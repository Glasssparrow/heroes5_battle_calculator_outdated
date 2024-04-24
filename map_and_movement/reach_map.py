

class ReachMap:

    def __init__(self, unit, length, height):
        self.threat_map_for_big_enemies = []
        self.threat_map_for_small_enemies = []
        self.map_length = length
        self.map_height = height
        self.enemy_big = False

    def __getitem__(self, coord):
        # Возвращает величину угрозы для выбранной клетки
        x, y = coord[0], coord[1]
        if self.enemy_big:
            return self.threat_map_for_big_enemies[x+y*self.map_length]
        else:
            return self.threat_map_for_small_enemies[x + y * self.map_length]