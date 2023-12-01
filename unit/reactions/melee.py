from keywords import *
from random import randint
from unit.common import calculate_damage


class MeleeCounter:

    def __init__(self, owner):
        self.owner = owner
        self.keyword = MELEE_COUNTER

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
        print(f"{self.owner.name} контратакует {target.name}. "
              f"Наносит {damage} урона. "
              f"Погибло {kills} {target.name}. "
              f"Осталось {target.quantity}")
