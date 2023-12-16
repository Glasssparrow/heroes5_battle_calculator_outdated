from .common import Effect
from keywords import *


class Block1Counterattack(Effect):

    def __init__(self):
        super().__init__()
        self.name = "block_1_counter"
        self.special_effects.append(TEMPORARY_BLOCK_COUNTER)
        self.dispell_conditions.append(DISPELL_TEMPORARY_BLOCK_COUNTER)
