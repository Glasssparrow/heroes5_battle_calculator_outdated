from .common import Effect


class DexterityBuff(Effect):

    def __init__(self):
        super().__init__()
        self.defence = 14
        self.name = "Ловкость (бафф)"

    def reapply(self, new_instance):
        self.defence = new_instance.defence


class DivineStrength(Effect):

    def __init__(self):
        super().__init__()
        self.name = "божественная сила"
        self.damage = 0.5
        self.time = 3
