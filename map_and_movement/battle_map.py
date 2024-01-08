

class BattleMap:

    def __init__(self):
        self.units = []
        self.sides = {}

    def add_unit(self, unit, color=None):
        if color:
            unit.color = color
        if unit.color not in self.sides.keys():
            self.sides[unit.color] = len(self.sides)
        unit.side = self.sides[unit.color]
        unit.id = len(self.units)
        self.units.append(unit)

    def get_distance(self, unit1, unit2):
        pass
