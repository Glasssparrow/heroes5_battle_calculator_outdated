from math import ceil


class Unit:

    def take_action(self, action_type, target):
        self.start_turn()
        self._action(action_type, target)
        self.end_turn()

    def start_turn(self):
        pass

    def _action(self, action_type, target):
        for action in self.actions:
            if action.keyword == action_type:
                action.act(target)
                return

    def end_turn(self):
        pass

    def provoke_counter(self, reaction_type, target):
        for reaction in self.reactions:
            if reaction.keyword == reaction_type:
                reaction.act(target)

    def apply_effect(self, effect):
        print(f"На {self.name} наложен эффект {effect.name}")
        self.effects.append(effect)

    def take_damage(self, damage):
        self.hp = self.hp - damage
        if self.hp == 0:
            self.hp = 0
        quantity_before = self.quantity
        self.quantity = ceil(self.hp / self.health)
        kills = quantity_before - self.quantity
        return kills

    def __init__(self, name, color, attack, defence,
                 min_damage, max_damage, health, initiative, speed):
        self.name = name
        self.color = color
        self.actions = []
        self.reactions = []
        self.effects = []
        self.skills = []
        self.immunities = []
        self.attack = attack
        self.defence = defence
        self._min_damage_limit = min_damage
        self.min_damage = min_damage
        self._max_damage_limit = max_damage
        self.max_damage = max_damage
        self.health = health
        self.initiative = initiative
        self.speed = speed
        self._max_quantity = 0
        self.quantity = 0
        self.hp = 0

    def get_quantity(self, quantity):
        self._max_quantity = quantity
        self.quantity = quantity
        self.hp = quantity * self.health

    def add_action(self, action):
        self.actions.append(action(self))

    def add_reaction(self, reaction):
        self.reactions.append(reaction(self))
