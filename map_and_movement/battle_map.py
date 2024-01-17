from .get_distance import get_distance
from .move_to import move_to
from .run_away import run_away
from .get_available_cells import get_available_cells
from .dijkstra_on_grid import Pathfinder


class BattleMap:

    def __init__(self):
        self.units = []
        self.sides = {}
        self.pathfinders_small = {}
        self.pathfinders_big = {}

    def create_pathfinders(self, map_height, map_length):
        for side_name in self.sides.keys():
            self.pathfinders_big[side_name] = Pathfinder(map_height,
                                                         map_length,)
            self.pathfinders_small[side_name] = Pathfinder(map_height,
                                                           map_length, )
        for side_name, units in self.sides.items():
            # Помечаем ячейку занятой для своей фракции
            for number in units:
                unit = self.units[number]
                x, y = unit.coord[0], unit.coord[1]
                self.pathfinders_small[side_name].occupy_cell(x, y)
                self.pathfinders_big[side_name].occupy_cell(x, y)
            # Блокируем ячейку для чужих фракций
            for side in self.sides.keys():
                if side == side_name:
                    continue
                for number in units:
                    unit = self.units[number]
                    x, y = unit.coord[0], unit.coord[1]
                    self.pathfinders_small[side].block_cell(x, y)
                    self.pathfinders_big[side].block_cell(x, y)

    def add_unit(self, unit, x, y, color=None):
        if color:
            unit.color = color
        if unit.color not in self.sides.keys():
            self.sides[unit.color] = [len(self.units),]
        else:
            self.sides[unit.color].append(len(self.units))
        unit.coord = (x, y)
        unit.pos = unit.coord[0] + unit.coord[1] * 12
        unit.side = self.sides[unit.color]
        unit.id = len(self.units)
        self.units.append(unit)

    def _add_unit_on_grid(self, unit):
        pass

    @staticmethod
    def get_distance(unit1, unit2):
        return get_distance(unit1, unit2)
    
    def get_available_cells(self, unit):
        return get_available_cells(
            pathfinder_big=self.pathfinders_big[unit.color],
            pathfinder_small=self.pathfinders_small[unit.color],
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
