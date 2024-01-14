

def get_available_cells(pathfinder_big, pathfinder_small, unit):
    x, y = unit.coord[0], unit.coord[1]
    if unit.big:
        return pathfinder_big(x, y, unit.speed)
    else:
        return pathfinder_small(x, y, unit.speed)
