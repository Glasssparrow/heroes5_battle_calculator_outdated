

class DecisionMaker:

    def add(self, coord1, coord2):
        self.height[len(self.coords)] = 0
        self.coords.append((coord1, coord2,))

    def __init__(self):
        # Список координат
        self.coords = []
        # Вес для каждой координаты (ключ = номер координаты в листе)
        self.height = {}

    def __getitem__(self, item):
        for n, coord in enumerate(self.coords):
            if coord == item:
                return self.height[n]
        raise Exception(f"{item} вне диапазона.")

    def __setitem__(self, key, value):
        number = None
        for n, coord in enumerate(self.coords):
            if coord == key:
                number = n
        if number is not None:
            self.height[number] += value

    def __delitem__(self, key):
        number = None
        for n, coord in enumerate(self.coords):
            if coord == key:
                number = n
        if number is not None:
            self.height[number] = 0
