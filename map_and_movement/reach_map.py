

class ReachMap:

    def __init__(self, unit, length, height):
        self.threat_for_big = []
        self.threat_for_small = []
        self.map_length = length
        self.map_height = height
        self.enemy_big = False

    def __getitem__(self, coord):
        # Возвращает величину угрозы для выбранной клетки
        x, y = coord[0], coord[1]
        if self.enemy_big:
            return self.threat_for_big[x + y * self.map_length]
        else:
            return self.threat_for_small[x + y * self.map_length]