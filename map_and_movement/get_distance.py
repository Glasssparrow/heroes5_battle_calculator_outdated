

def get_distance(unit1, unit2):
    if not unit1.big and not unit2.big:
        x_distance = abs(unit1.coord[0] - unit2.coord[0])
        y_distance = abs(unit1.coord[1] - unit2.coord[1])
        if x_distance == y_distance == 1:
            return 1
        else:
            return x_distance+y_distance
