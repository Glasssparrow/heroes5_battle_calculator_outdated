from .common import Skill
from keywords import *


class Kill1Extra(Skill):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "Убивает на 1 существо больше"
        self.activation_cases.append(ACTIVATE_AFTER_STRIKE)

    @staticmethod
    def use(target, damage, kills, battle_map):
        killed_by_skill = target.take_damage(target.health)
        print(f"{target.name} получает {damage} урона. Погибло "
              f"{killed_by_skill} существ.")
