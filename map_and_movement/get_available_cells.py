from .dijkstra_on_grid import Path


class DangerZone:

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


def get_danger_zone(battle_map, unit):
    danger_zone = Path(unit.coord[0], unit.coord[1],
                       battle_map._map_length)
    for side_name, unit_ids_list in battle_map.sides.items():
        pass
