from .common import Skill
from keywords import *


class HighMorale(Skill):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "Воодушевление"
        self.keyword = ACTIVATE_AT_TURN_START

    def use(self):
        pass


class LowMorale(Skill):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "Нерешительность"
        self.keyword = ACTIVATE_AT_TURN_END

    def use(self):
        pass
