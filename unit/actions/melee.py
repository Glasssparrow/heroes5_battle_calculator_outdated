from keywords import *
from math import copysign, floor
from random import randint


def calculate_damage(damage, attack, defence, max_damage):
    sign = copysign(1, attack - defence)
    amount_of_damage = (
        damage * (1 + 0.05 * abs(attack - defence)) ** sign
    )
    # По игровой механике урон округляется вниз
    amount_of_damage = floor(amount_of_damage)
    if amount_of_damage > max_damage:
        return max_damage
    else:
        return amount_of_damage


class Melee:

    def __init__(self, owner):
        self.owner = owner
        self.keyword = MELEE_ATTACK

    def act(self, target):
        min_damage = self.owner.min_damage * self.owner.quantity
        max_damage = self.owner.max_damage * self.owner.quantity
        damage = calculate_damage(
            damage=randint(min_damage, max_damage),
            attack=self.owner.attack,
            defence=target.defence,
            max_damage=target.hp
        )
        kills = target.take_damage(damage)
        print(f"{self.owner.name} атакует {target.name}. "
              f"Наносит {damage} урона. "
              f"Погибло {kills} {target.name}. "
              f"Осталось {target.quantity}")
