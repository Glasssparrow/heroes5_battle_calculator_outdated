from .common import Skill, calculate_base_chance
from ..common import check_random
from unit.effects import *
from keywords import *


class PeasantBash(Skill):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "Наложение дебафа"
        self.activation_cases.append(ACTIVATE_BEFORE_STRIKE)

    def use(self, target, damage, kills, battle_map):
        if check_random(self.get_chance(target)):
            print(f"наложен {Block1Counterattack().name}")
            target.apply_effect(Block1Counterattack())
            target.apply_effect(Bash())

    @staticmethod
    def _chance_formula(base_chance):
        return 1-(1-base_chance)**1

    def get_chance(self, target):
        chance = self._chance_formula(
            calculate_base_chance(self.owner, target)
        )
        if chance < 0.05:
            return 0.05
        elif chance > 0.75:
            return 0.75
        else:
            return chance


class FootmanBash(PeasantBash):

    @staticmethod
    def _chance_formula(base_chance):
        return 1-(1-base_chance)**1.5
