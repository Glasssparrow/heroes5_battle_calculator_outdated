from .common import Effect


class Plus5Attack(Effect):

    def __init__(self):
        super().__init__()
        self.attack = 5
