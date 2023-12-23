from math import ceil
from .stats import *
from .skills.turnend import *


# Класс отвечающий за взаимодействие между юнитами.
# Не отвечает за шкалу инициативы и передвижение.
# Экземпляры класса лишь хранят положение на поле и шкале инициативы.
# Наложение аур связано с передвижением, поэтому также обрабатывается вне
# класса.
class Unit:

    attack = Stat()
    defence = Stat()
    min_damage = MinDamage()
    max_damage = MaxDamage()
    health = Health()
    initiative = Initiative()
    speed = Speed()
    luck = Luck()
    morale = Morale()

    def take_action(self, action_type, target, battle_map):
        self.start_turn()
        self._action(action_type, target, battle_map)
        self.end_turn()

    def start_turn(self):
        self.dispell_by_case(DISPELL_AT_TURN_START)
        for skill in self.turnend_skills:
            if ACTIVATE_AT_TURN_START in skill.activation_cases:
                skill.use()
                return

    def _action(self, action_type, target, battle_map):
        for action in self.actions:
            if action.keyword == action_type:
                action.act(target, battle_map)
                return

    def end_turn(self):
        self.dispell_by_case(DISPELL_AT_TURN_END)
        for skill in self.turnend_skills:
            if ACTIVATE_AT_TURN_END in skill.activation_cases:
                skill.use()
        self.tiles_moved = 0  # После срабатывания всех эффектов

    def react(self, reaction_type, target, battle_map):
        for reaction in self.reactions:
            if reaction.keyword == reaction_type:
                reaction.react(target, battle_map)

    def use_skills(
            self, skill_type, target, battle_map, damage=0, kills=0
    ):
        for skill in self.skills:
            if skill_type in skill.activation_cases:
                skill.use(target, damage, kills, battle_map)

    def apply_effect(self, new_effect):
        for effect in self.effects:
            if new_effect.name == effect.name:
                effect.reapply(new_effect)
                print(f"На {self.name} переналожен эффект "
                      f"{effect.name}")
                return
        print(f"На {self.name} наложен эффект {new_effect.name}")
        self.effects.append(new_effect)

    def take_damage(self, damage):
        self.hp = self.hp - damage
        if self.hp < 0:
            self.hp = 0
        quantity_before = self.quantity
        self.quantity = ceil(self.hp / self.health)
        kills = quantity_before - self.quantity
        return kills

    def take_healing(self, healing):
        self.hp = self.hp + healing
        if self.hp > self._max_quantity * self.health:
            self.hp = self._max_quantity * self.health
        quantity_before = self.quantity
        self.quantity = self.hp / self.health
        revived = self.quantity - quantity_before
        return revived

    def __init__(self, name, color, attack, defence,
                 min_damage, max_damage, health, initiative, speed):
        self.name = name
        self.color = color
        self.actions = []
        self.reactions = []
        self.skills = []
        self.turnend_skills = [HighMorale(owner=self),
                               LowMorale(owner=self)]
        self.auras = []
        self.effects = []
        self.immunities = []
        self.special_attributes = []
        self.attack = attack
        self.defence = defence
        self._min_damage_limit = min_damage
        self.min_damage = min_damage
        self._max_damage_limit = max_damage
        self.max_damage = max_damage
        self._health = health
        self.initiative = initiative
        self.speed = speed
        self._max_quantity = 0
        self.quantity = 0
        self.hp = 0
        self.luck = 0
        self.morale = 0

        self.tiles_moved = 0

    def get_quantity(self, quantity):
        self._max_quantity = quantity
        self.quantity = quantity
        self.hp = quantity * self.health

    def add_action(self, action):
        self.actions.append(action(self))

    def add_reaction(self, reaction):
        self.reactions.append(reaction(self))

    def add_skill(self, skill):
        self.skills.append(skill(self))

    def add_turnend_skill(self, skill):
        self.turnend_skills.append(skill(self))

    def add_aura(self, aura):
        self.auras.append(aura)

    def dispell_by_case(self, dispell_trigger):
        for_delete = []
        for number, effect in enumerate(self.effects):
            if dispell_trigger in effect.dispell_conditions:
                if effect.dispell_exception_once:
                    print(f"Использован 1 жетон иммунитета к снятию "
                          f"{effect.name}")
                    effect.dispell_exception_once = False
                else:
                    for_delete.append(number)
        for x in reversed(for_delete):
            print(f"{self.name}. Эффект {self.effects[x].name} снят")
            self.effects.pop(x)

    def check_immunity(self, immunity_keyword):
        if not self.immunities:
            return False
        for immunity in self.immunities:
            if immunity == immunity_keyword:
                return True
        return False
