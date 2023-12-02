from keywords import *
from random import randint
from unit.common import calculate_damage
from .common import Action


class Melee(Action):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "Атака в ближнем бою"
        self.keyword = MELEE_ATTACK

    def act(self, target):
        if not self.can_unit_act(target):
            return
        min_damage = self.owner.min_damage * self.owner.quantity
        max_damage = self.owner.max_damage * self.owner.quantity
        damage = calculate_damage(
            damage=randint(min_damage, max_damage),
            attack=self.owner.attack,
            defence=target.defence,
            max_damage=target.hp
        )
        self.before_action(target)
        kills = target.take_damage(damage)
        self.after_action(target, damage, kills)
        print(f"{self.owner.name} атакует {target.name}. "
              f"Наносит {damage} урона. "
              f"Погибло {kills} {target.name}. "
              f"Осталось {target.quantity}")
        target.react(MELEE_COUNTER, self.owner)

    def can_unit_act(self, target):
        if not self.owner.hp > 0:
            print(f"{self.owner.name} не может действовать т.к. мертв.")
            return False
        if target.hp == 0:
            print(f"{self.owner.name} не может действовать т.к. "
                  f"цель мертва.")
            return False
        return True

    def before_action(self, target):
        self.owner.use_skills(ACTIVATE_BEFORE_STRIKE, target)

    def after_action(self, target, damage, kills):
        self.owner.use_skills(ACTIVATE_AFTER_STRIKE, target)
