from .dijkstra_on_grid import Path


class BlockableDangerZone:

    def __init__(self, length, height, data):
        self._length = length
        self._height = height
        self._blockable_danger = data
        for x in range(length):
            self._blockable_danger.append([0] * height)

    def __getitem__(self, item):
        return self._blockable_danger[item[0]][item[1]]

    def __setitem__(self, key, value):
        if not isinstance(value, (float, int)):
            raise Exception(
                f"Допустимо лишь float/int, получено - {value}"
            )
        if 0 <= key[0] < self._length and 0 <= key[1] < self._height:
            self._blockable_danger[key[0]][key[1]] = value

    def __delitem__(self, key):
        self._blockable_danger[key[0]][key[1]] = 0


class DangerZone:

    def __init__(self, length, height):
        self.length = length
        self.height = height
        self._danger = []
        self._blockable_danger = []
        self._blockable_danger_instance = BlockableDangerZone(
            length=length,
            height=height,
            data=self._blockable_danger,
        )
        for x in range(length):
            self._danger.append([0] * height)
            self._blockable_danger.append([0] * height)

    @property
    def blockable(self):
        return self._blockable_danger_instance

    def __getitem__(self, item):
        return self._danger[item[0]][item[1]]

    def __setitem__(self, key, value):
        if not isinstance(value, (float, int)):
            raise Exception(
                f"Допустимо лишь float/int, получено - {value}"
            )
        if 0 <= key[0] < self.length and 0 <= key[1] < self.height:
            self._danger[key[0]][key[1]] = value

    def __delitem__(self, key):
        self._danger[key[0]][key[1]] = 0


class DangerZoneInProgress:

    def __init__(self, height, length):
        self.height = height
        self.length = length
        self.data = []
        self.danger_map = []
        for x in range(length):
            self.data.append([False]*height)
            self.danger_map.append([0]*height)
        self.danger = 0

    def set_skill_danger_level(self, danger_level):
        self.danger = danger_level

    def add_danger(self):
        for x in range(self.length):
            for y in range(self.height):
                if (
                    self.data[x][y] and
                    self.danger_map[x][y] < self.danger
                ):
                    self.danger_map[x][y] = self.danger

    def get_danger(self, item):
        return self.danger_map[item[0]][item[1]]

    def __getitem__(self, item):
        return self.data[item[0]][item[1]]

    def __setitem__(self, key, value):
        if not isinstance(value, bool):
            raise Exception(
                f"Допустимо лишь True/False, получено - {value}"
            )
        self.data[key[0]][key[1]] = value

    def __delitem__(self, key):
        self.data[key[0]][key[1]] = False


def get_available_cells(pathfinder_big, pathfinder_small, unit):
    x, y = unit.coord[0], unit.coord[1]
    # Возвращает экземпляр класса Path
    if unit.big:
        return pathfinder_big(x, y, unit.speed)
    else:
        return pathfinder_small(x, y, unit.speed)


def get_attack_area(x, y, big):
    attack_area = []
    if big:
        for dx, dy in [
            (0, 1), (1, 1), (1, 0), (1, -1),
            (0, -1), (-1, -1), (-1, 0), (-1, 1),
        ]:
            attack_area.append((x+dx, y+dy))
    else:
        for dx, dy in [
            (0, -1), (+1, -1,), (+2, -1),
            (+2, 0), (+2, +1), (+2, +2),
            (+1, +2), (0, +2), (-1, +2),
            (-1, +1), (-1, 0), (-1, -1)
        ]:
            attack_area.append((x + dx, y + dy))
    return attack_area


def get_danger_zone(battle_map, the_unit):
    result = DangerZone(
        height=battle_map.map_height,
        length=battle_map.map_length,
    )
    for side_color, unit_ids_list in battle_map.sides.items():
        if side_color == the_unit.color:
            continue
        for unit_id in unit_ids_list:
            unit = battle_map.units[unit_id]
            danger_tmp = DangerZoneInProgress(
                height=battle_map.map_height,
                length=battle_map.map_length,
            )
            available_cells = battle_map.get_available_cells(unit)
            for coord, length, path in available_cells:
                attack_area = get_attack_area(
                    x=coord[0], y=coord[1],
                    big=unit.big,
                )
                for cell in attack_area:
                    pass
    return result

    # Возвращаем экземпляр класса DangerZone
