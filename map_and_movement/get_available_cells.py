from .dijkstra_on_grid import Path


class DangerZone:

    def __init__(self, height, length):
        self.height = height
        self.length = length
        self.data = []
        for x in range(length):
            self.data.append([False]*height)


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
