

def act(unit, battle_map):
    available_cells = battle_map.get_available_cells(unit)
    for coord, length, path in available_cells:
        print(coord, length, path)
        pass
