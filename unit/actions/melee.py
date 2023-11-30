from keywords import *
from math import copysign


def calculate_damage(damage, attack, defence):
    sign = copysign(1, attack - defence)
    amount_of_damage = (
        damage * (1 + 0.05 * abs(attack - defence)) ** sign
    )
    amount_of_damage = round(amount_of_damage, 0)
    return amount_of_damage


class Melee:

    def __init__(self, owner):
        self.owner = owner
        self.keyword = MELEE_ATTACK

    def act(self, target):
        print(f"{self.owner.name} атакует {target.name}")
