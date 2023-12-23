from .common import Effect
from keywords import *


class Block1Counterattack(Effect):

    def __init__(self):
        super().__init__()
        self.name = "block_1_counter"
        self.special_effects.append(TEMPORARY_BLOCK_COUNTER)
        self.dispell_conditions.append(DISPELL_TEMPORARY_BLOCK_COUNTER)


class Blind(Effect):

    def __init__(self):
        super().__init__()
        self.name = "ослепление"
        self.special_effects.append(BLOCK_ACTION)
        self.special_effects.append(BLOCK_COUNTER)
        self.dispell_conditions.append(DISPELL_AFTER_TAKING_DAMAGE)


class BlindFromStrike(Blind):

    def __init__(self):
        super().__init__()
        self.dispell_exception_once = True
        self.name = "ослепление (от удара)"


class Plague(Effect):

    def __init__(self):
        super().__init__()
        self.name = "чумной удар"
        self.attack = -2
        self.defence = -2

    def reapply(self, new_instance):
        self.attack += -2
        self.defence += -2
