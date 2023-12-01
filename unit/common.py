from math import copysign, floor


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
