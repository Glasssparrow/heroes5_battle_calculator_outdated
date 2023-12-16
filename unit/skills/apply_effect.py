from .common import Skill
from ..common import check_random
from unit.effects.debuffs import *
from keywords import *


class PeasantBash(Skill):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "Наложение дебафа"
        self.effect = Block1Counterattack()
        self.activation_cases.append(ACTIVATE_BEFORE_STRIKE)

    def use(self, target, damage, kills, battle_map):
        if check_random(self.get_chance(target)):
            print(f"наложен {self.effect.name}")
            target.apply_effect(self.effect)

    def _calculate_base_chance(self, target):
        if self.owner.hp < target.hp:
            return 0.25 + self.owner.hp/target.hp
        else:
            return 0.25 - target.hp/self.owner.hp

    @staticmethod
    def _chance_formula(base_chance):
        return 1-(1-base_chance)**1

    def get_chance(self, target):
        chance = self._chance_formula(
            self._calculate_base_chance(target)
        )
        if chance < 0.05:
            return 0.05
        elif chance > 0.75:
            return 0.75
        else:
            return chance
