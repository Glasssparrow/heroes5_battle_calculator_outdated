

class Unit:

    def take_action(self, action_type, target):
        self._start_turn()
        self._action(action_type, target)
        self._end_turn()

    def _start_turn(self):
        pass

    def _action(self, action_type, target):
        pass

    def _end_turn(self):
        pass

    def __init__(self, attack, defence, min_damage, max_damage, health,
                 initiative, speed):
        self.actions = []
        self.reactions = []
        self.effects = []
        self.skills = []
        self.immunities = []
        self.atk = attack
        self.defence = defence
        self.min_damage_limit = min_damage
        self.min_damage = min_damage
        self.max_damage_limit = max_damage
        self.max_damage = max_damage
        self.health = health
        self.initiative = initiative
        self.speed = speed
        self.quantity = 0
        self.hp = 0

    def get_quantity(self, quantity):
        self.quantity = quantity
        self.hp = quantity * self.health
