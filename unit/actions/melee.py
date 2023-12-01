from keywords import *
from random import randint
from unit.common import calculate_damage


class Melee:

    def __init__(self, owner):
        self.name = "Атака в ближнем бою"
        self.owner = owner
        self.keyword = MELEE_ATTACK

    def act(self, target):
        if not self.can_unit_act():
            return
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
        target.provoke_counter(MELEE_COUNTER, self.owner)

    def can_unit_act(self):
        if not self.owner.hp > 0:
            print(f"{self.owner.name} не может действовать т.к. мертв")
            return False
        return True
