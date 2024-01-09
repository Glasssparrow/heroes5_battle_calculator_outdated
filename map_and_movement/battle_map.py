from .get_distance import get_distance
from .move_to import move_to
from .run_away import run_away
from .get_available_cells import get_available_cells
from random import randint


class BattleMap:

    def __init__(self):
        self.units = []
        self.sides = {}

    def add_unit(self, unit, color=None):
        if color:
            unit.color = color
        if unit.color not in self.sides.keys():
            self.sides[unit.color] = len(self.sides)
        if not unit.coord:
            unit.coord = (randint(1, 10), randint(1, 12))
        unit.side = self.sides[unit.color]
        unit.id = len(self.units)
        self.units.append(unit)

    @staticmethod
    def get_distance(unit1, unit2):
        return get_distance(unit1, unit2)
    
    def get_available_cells(self, unit):
        return get_available_cells(self, unit)

    def move_to(self, unit, coord):
        move_to(self, unit, coord)

    def run_away(self, coward, scary_unit):
        run_away(self, coward, scary_unit)

    def get_visualisation(self):
        pass
