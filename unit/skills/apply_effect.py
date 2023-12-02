from .common import Skill
from unit.effects.debuffs import Debuff
from keywords import *


class ApplyTestEffect(Skill):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "Наложение дебафа"
        self.effect = Debuff()
        self.keyword = ACTIVATE_BEFORE_STRIKE

    def use(self, target):
        target.apply_effect(self)
