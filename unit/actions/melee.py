from keywords import *
from random import randint
from ..common import calculate_damage
from .common import Action


class Melee(Action):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "Атака в ближнем бою"
        self.keyword = MELEE_ATTACK

    def act(self, target, battle_map):
        if not self.can_unit_act(target, battle_map):
            return
        self.strike(target, battle_map)
        target.react(MELEE_COUNTER, self.owner, battle_map)

    def strike(self, target, battle_map):
        if not self.is_melee_attack_possible(target, battle_map):
            return 0
        damage_modifier = self.calculate_damage_modifier()
        min_damage = int(
            self.owner.min_damage * self.owner.quantity * damage_modifier
        )
        max_damage = int(
            self.owner.max_damage * self.owner.quantity * damage_modifier
        )
        damage = calculate_damage(
            damage=randint(min_damage, max_damage),
            attack=self.owner.attack,
            defence=target.defence,
            max_damage=target.hp
        )
        self.before_action(target, battle_map)
        kills = target.take_damage(damage)
        print(f"{self.owner.name} атакует {target.name}. "
              f"Наносит {damage} урона. "
              f"Погибло {kills} {target.name}. "
              f"Осталось {target.quantity}")
        self.after_action(target, damage, kills, battle_map)
        return kills

    def can_unit_act(self, target, battle_map):
        if not self.owner.hp > 0:
            print(f"{self.owner.name} не может действовать т.к. мертв.")
            return False
        if not target.hp > 0:
            print(f"{self.owner.name} не может действовать т.к. "
                  f"цель мертва.")
            return False
        for effect in self.owner.effects:
            if BLOCK_ACTION in effect.special_effects:
                print(f"{self.owner.name} ожидает в нерешительности.")
                return False
        return True

    @staticmethod
    def is_melee_attack_possible(target, battle_map):
        return True

    def before_action(self, target, battle_map):
        self.owner.use_skills(ACTIVATE_BEFORE_STRIKE, target, battle_map)

    def after_action(self, target, damage, kills, battle_map):
        self.owner.use_skills(
            ACTIVATE_AFTER_STRIKE, target, damage, kills, battle_map
        )


class ChivalryCharge(Melee):

    def calculate_damage_modifier(self):
        damage_modifier = 1 + 0.05 * self.owner.tiles_moved
        damage_modifier = damage_modifier * self.luck_modifier()
        return damage_modifier


class DoubleAttackIfKill(Melee):

    def act(self, target, battle_map):
        if not self.can_unit_act(target, battle_map):
            return
        kills = self.strike(target, battle_map)
        target.react(MELEE_COUNTER, self.owner, battle_map)
        if kills > 0:
            self.strike(target, battle_map)
            target.react(MELEE_COUNTER, self.owner, battle_map)


class DoubleAttack(Melee):

    def act(self, target, battle_map):
        if not self.can_unit_act(target, battle_map):
            return
        self.strike(target, battle_map)
        target.react(MELEE_COUNTER, self.owner, battle_map)
        self.strike(target, battle_map)
        target.react(MELEE_COUNTER, self.owner, battle_map)


class MeleeNoCounter(Melee):

    def act(self, target, battle_map):
        if not self.can_unit_act(target, battle_map):
            return
        self.strike(target, battle_map)


class WeakMelee(Melee):

    def calculate_damage_modifier(self):
        damage_modifier = 0.5
        damage_modifier = damage_modifier * self.luck_modifier()
        return damage_modifier
