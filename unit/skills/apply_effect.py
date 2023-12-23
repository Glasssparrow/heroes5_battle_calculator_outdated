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
        if (
            check_random(self.get_chance(target)) and
            not target.check_immunity(VAMPIRISM_IMMUNE)
        ):
            print(f"наложен {Block1Counterattack().name}")
            target.apply_effect(Block1Counterattack())
            target.apply_effect(Bash())
        else:
            print(f"У {target.name} иммунитет оглушению")

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


class BlindingStrike(PeasantBash):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "Ослепляющий удар"

    def use(self, target, damage, kills, battle_map):
        if (
            check_random(self.get_chance(target)) and
            not target.check_immunity(BLIND_IMMUNE)
        ):
            target.apply_effect(BlindFromStrike())
        else:
            if target.check_immunity(BLIND_IMMUNE):
                print(f"{target.name} иммунитет ослеплению")
            else:
                print(f"Ослепляющий удар не сработал")

    @staticmethod
    def _chance_formula(base_chance):
        return 1-(1-base_chance)**1


class PlagueStrike(Skill):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "Чумной удар"
        self.activation_cases.append(ACTIVATE_AFTER_STRIKE)

    @staticmethod
    def use(target, damage, kills, battle_map):
        target.apply_effect(Plague())
