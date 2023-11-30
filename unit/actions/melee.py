from keywords import *
from math import copysign, floor


def calculate_damage(damage, attack, defence):
    sign = copysign(1, attack - defence)
    amount_of_damage = (
        damage * (1 + 0.05 * abs(attack - defence)) ** sign
    )
    # По игровой механике урон округляется вниз
    amount_of_damage = floor(amount_of_damage)
    return amount_of_damage


class Melee:

    def __init__(self, owner):
        self.owner = owner
        self.keyword = MELEE_ATTACK

    def act(self, target):
        print(f"{self.owner.name} атакует {target.name}")
