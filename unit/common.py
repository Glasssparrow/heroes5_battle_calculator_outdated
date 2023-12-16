from math import copysign, floor
from random import random


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


def check_random(chance):
    if not isinstance(chance, (int, float)):
        raise Exception(
            "Не верный тип данных"
        )
    if chance < 0 or chance > 1:
        raise Exception(
            "Не в промежутке 0 < chance < 1"
        )
    if chance > random():
        return True
    else:
        return False
