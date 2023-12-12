from .common import Skill
from ..effects import *
from keywords import *


class HighMorale(Skill):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "+Мораль"
        self.keyword = ACTIVATE_AT_TURN_END

    def use(self):
        self.owner.apply_effect(HighMoraleEffect())


class LowMorale(Skill):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "-Мораль"
        self.keyword = ACTIVATE_AT_TURN_START

    def use(self):
        self.owner.apply_effect(LowMoraleEffect())
