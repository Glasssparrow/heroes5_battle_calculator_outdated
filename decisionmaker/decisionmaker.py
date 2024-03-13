

class DecisionMaker:

    def __init__(self):
        self.coords = []
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
        if number is None:
            raise Exception(f"{key} вне диапазона")
        else:
            self.height[number] += value

    def __delitem__(self, key):
        number = None
        for n, coord in enumerate(self.coords):
            if coord == key:
                number = n
        if number is None:
            raise Exception(f"{key} вне диапазона")
        else:
            self.height[number] = 0
