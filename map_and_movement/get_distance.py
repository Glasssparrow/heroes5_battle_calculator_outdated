

def get_distance(unit1, unit2):
    if not unit1.big and not unit2.big:
        x_distance = abs(unit1.coord[0] - unit2.coord[0])
        y_distance = abs(unit1.coord[1] - unit2.coord[1])
        if x_distance == y_distance == 1:
            return 1
        else:
            return x_distance+y_distance
    unit1_coord = {0: None, 1: None}
    unit2_coord = {0: None, 1: None}
    for axis in (0, 1):
        if unit1.coord[axis] > unit2.coord[axis]:
            unit1_coord[axis] = unit1.coord[axis]
            if unit2.big:
                unit2_coord[axis] = unit2.coord[axis] + 1
            else:
                unit2_coord[axis] = unit2.coord[axis]
        elif unit1.coord[axis] < unit2.coord[axis]:
            unit2_coord[axis] = unit2.coord[axis]
            if unit1.big:
                unit1_coord[axis] = unit1.coord[axis] + 1
            else:
                unit1_coord[axis] = unit1.coord[axis]
        else:
            unit1_coord[axis] = unit1.coord[axis]
            unit2_coord[axis] = unit2.coord[axis]
    x_distance = abs(unit1_coord[0] - unit2_coord[0])
    y_distance = abs(unit1_coord[1] - unit2_coord[1])
    if x_distance == y_distance == 1:
        return 1
    else:
        return x_distance + y_distance
