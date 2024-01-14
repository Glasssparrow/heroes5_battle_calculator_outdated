from .get_distance import get_distance
from .move_to import move_to
from .run_away import run_away
from .get_available_cells import get_available_cells
from random import randint
from .dijkstra_on_grid import Pathfinder


class BattleMap:

    def __init__(self):
        self.units = []
        self.sides = {}
        self.pathfinder_small = Pathfinder(10, 12)
        self.pathfinder_big = Pathfinder(10, 12)

    def add_unit(self, unit, color=None):
        if color:
            unit.color = color
        if unit.color not in self.sides.keys():
            self.sides[unit.color] = len(self.sides)
        if not unit.coord:
            unit.coord = (randint(1, 10), randint(1, 12))
        unit.pos = unit.coord[0] + unit.coord[1] * 12
        unit.side = self.sides[unit.color]
        unit.id = len(self.units)
        self.units.append(unit)

    @staticmethod
    def get_distance(unit1, unit2):
        return get_distance(unit1, unit2)
    
    def get_available_cells(self, unit):
        return get_available_cells(
            pathfinder_big=self.pathfinder_big,
            pathfinder_small=self.pathfinder_small,
            unit=unit,
        )

    def move_to(self, unit, coord):
        move_to(self, unit, coord)

    def run_away(self, coward, scary_unit):
        run_away(self, coward, scary_unit)

    def get_visualisation(self):
        visualisation = []
        for line in range(10):
            visualisation.append(["  .  "]*12)
        for unit in self.units:
            coord = unit.coord
            visualisation[coord[1]][coord[0]] = unit.color
            if unit.big:
                for x, y in [(0, 1), (1, 0), (1, 1)]:
                    visualisation[coord[1]+y][coord[0]+x] = unit.color
        picture = ""
        for line in reversed(visualisation):
            for x in line:
                picture += x[0:5]
            picture += "\n"
        return picture
