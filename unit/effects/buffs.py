from .common import Effect


class TestPlusStat(Effect):

    def __init__(self):
        super().__init__()
        self.defence = 5
        self.name = "Buff"
