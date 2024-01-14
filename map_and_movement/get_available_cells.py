from .dijkstra_on_grid import Pathfinder


def get_available_cells(battle_map, unit):
    pathfinder = Pathfinder(10, 12)
    return pathfinder(unit.coord[0], unit.coord[1], unit.speed)
