from .common import Effect
from keywords import *


class LowMorale(Effect):

    def __init__(self):
        super().__init__()
        self.initiative_mark = INITIATIVE_MORALE
        self.special_effects.append(BLOCK_ACTION)
        self.dispell_conditions = [DISPELL_CASE_INITIATIVE]


class HighMorale(Effect):

    def __init__(self):
        super().__init__()
        self.initiative_mark = INITIATIVE_MORALE
        self.dispell_conditions = [DISPELL_CASE_INITIATIVE]
