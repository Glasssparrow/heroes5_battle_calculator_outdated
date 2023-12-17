from random import randint
from ..common import calculate_damage
from .common import Reaction
from ..effects.counterattack import *


class MeleeCounter(Reaction):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "Контратака в ближнем бою"
        self.owner = owner
        self.keyword = MELEE_COUNTER

    def react(self, target, battle_map):
        if not self.can_unit_react(target, battle_map):
            return
        if self.failed_counter():
            return
        self.strike(target, battle_map)

    def strike(self, target, battle_map):
        min_damage = (
            self.owner.min_damage * self.owner.quantity *
            self.calculate_damage_modifier()
        )
        max_damage = (
            self.owner.max_damage * self.owner.quantity *
            self.calculate_damage_modifier()
        )
        damage = calculate_damage(
            damage=randint(min_damage, max_damage),
            attack=self.owner.attack,
            defence=target.defence,
            max_damage=target.hp
        )
        self.before_reaction(target, battle_map)
        kills = target.take_damage(damage)
        self.after_reaction(target, damage, kills, battle_map)
        print(f"{self.owner.name} контратакует {target.name}. "
              f"Наносит {damage} урона. "
              f"Погибло {kills} {target.name}. "
              f"Осталось {target.quantity}")

    @staticmethod
    def calculate_damage_modifier():
        return 1

    def can_unit_react(self, target, battle_map):
        if not self.owner.hp > 0:
            print(f"{self.owner.name} не может реагировать т.к. мертв")
            return False
        if target.hp == 0:
            print(f"{self.owner.name} не может действовать т.к. "
                  f"цель мертва.")
            return False
        for effect in self.owner.effects:
            if BLOCK_COUNTER in effect.special_effects:
                print(f"{self.owner.name} не может контратаковать "
                      f"т.к. эффект {effect.name} блокирует эту "
                      f"возможность.")
                return False
        return True

    def before_reaction(self, target, battle_map):
        self.owner.use_skills(ACTIVATE_BEFORE_STRIKE, target, battle_map)

    def after_reaction(self, target, damage, kills, battle_map):
        self.owner.use_skills(
            ACTIVATE_AFTER_STRIKE, target, damage, kills, battle_map
        )
        self.owner.apply_effect(BlockCounter())

    def failed_counter(self):
        failed = False
        for number, effect in enumerate(self.owner.effects):
            if TEMPORARY_BLOCK_COUNTER in effect.special_effects:
                failed = True
                break
        if failed:
            self.owner.dispell_by_case(DISPELL_TEMPORARY_BLOCK_COUNTER)
            return True
        else:
            return False


class InfiniteMeleeCounter(MeleeCounter):

    def after_reaction(self, target, damage, kills, battle_map):
        self.owner.use_skills(
            ACTIVATE_AFTER_STRIKE, target, damage, kills, battle_map
        )


class BattleFrenzyCounter(MeleeCounter):

    def after_reaction(self, target, damage, kills, battle_map):
        self.owner.use_skills(
            ACTIVATE_AFTER_STRIKE, target, damage, kills, battle_map
        )
        self.owner.apply_effect(BattleFrenzy())
