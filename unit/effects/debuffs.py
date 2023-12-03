from .common import Effect


class Debuff(Effect):

    def __init__(self):
        super().__init__()
        self.defence = -5
        self.name = "Debuff"
