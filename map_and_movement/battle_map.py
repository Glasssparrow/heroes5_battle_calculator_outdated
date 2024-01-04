

class BattleMap:

    def __init__(self):
        self.units = []

    def add_unit(self, unit, color=None):
        if color:
            unit.color = color
        self.units.append(unit)
