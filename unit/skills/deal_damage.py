from .common import Skill
from keywords import *
from random import randint
from ..common import calculate_damage


class Kill1Extra(Skill):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "Убивает на 1 существо больше"
        self.activation_cases.append(ACTIVATE_BEFORE_STRIKE)

    @staticmethod
    def use(target, damage, kills, battle_map):
        killed_by_skill = target.take_damage(target.health)
        print(f"{target.name} получает {target.health} урона. Погибло "
              f"{killed_by_skill} существ.")


class Deal2DamageToEach(Skill):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "2 урона каждому существу"
        self.activation_cases.append(ACTIVATE_BEFORE_STRIKE)

    @staticmethod
    def use(target, damage, kills, battle_map):
        quantity = target.quantity*2
        killed_by_skill = target.take_damage(target.quantity*2)
        print(f"{target.name} получает {quantity} урона. Погибло "
              f"{killed_by_skill} существ.")


class ThunderStrike(Skill):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "Удар бури"
        self.activation_cases.append(ACTIVATE_AFTER_STRIKE)

    def use(self, target, damage, kills, battle_map):
        min_damage = int(
            self.owner.min_damage * self.owner.quantity
        )
        max_damage = int(
            self.owner.max_damage * self.owner.quantity
        )
        damage = calculate_damage(
            damage=randint(min_damage, max_damage),
            attack=self.owner.attack,
            defence=target.defence,
            max_damage=target.hp
        )
        kills = target.take_damage(damage)
        print(f"{self.owner.name} наносит {target.name}. "
              f"{damage} урона при помощи удара бури. "
              f"Погибло {kills} {target.name}. "
              f"Осталось {target.quantity}")
