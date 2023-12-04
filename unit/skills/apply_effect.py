from .common import Skill
from unit.effects.debuffs import *
from keywords import *


class ApplyTestEffect(Skill):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "Наложение дебафа"
        self.effect = Debuff()
        self.keyword = ACTIVATE_BEFORE_STRIKE

    @staticmethod
    def use(target, damage, kills, battle_map):
        target.apply_effect(Debuff())
