from get_distance import get_distance
from move_to import move_to
from run_away import run_away


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
        get_distance(self, unit1, unit2)

    def move_to(self, unit, coord):
        move_to(self, unit, coord)

    def run_away(self, coward, scary_unit):
        run_away(self, coward, scary_unit)

    def get_visualisation(self):
        pass
