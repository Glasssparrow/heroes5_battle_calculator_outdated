from .common import Effect
from keywords import *


class BattleFrenzy(Effect):

    def __init__(self):
        super().__init__()
        self.name = "battle_frenzy"
        self.modifiers[BATTLE_FRENZY_MODIFIER] = 1.5
        self.dispell_conditions.append(DISPELL_AT_TURN_START)

    def reapply(self, new_instance):
        self.modifiers[BATTLE_FRENZY_MODIFIER] = (
            self.modifiers[BATTLE_FRENZY_MODIFIER] * 1.5
        )
