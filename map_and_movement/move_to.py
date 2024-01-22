

def move_to(battle_map, unit, coord):
    unit.tiles_moved = (
        abs(unit.coord[0]-coord[0]) + abs(unit.coord[1]-coord[1])
    )
    unit.coord = coord[0], coord[1]
