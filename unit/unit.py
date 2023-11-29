

class Unit:

    def take_action(self, action_type, target):
        self._start_turn()
        self._action(action_type, target)
        self._end_turn()

    def _start_turn(self):
        pass

    def _action(self, action_type, target):
        for action in self.actions:
            if action.keyword == action_type:
                action.act(target)

    def _end_turn(self):
        pass

    def _counter_provoked(self):
        pass

    def __init__(self, name, color, attack, defence,
                 min_damage, max_damage, health, initiative, speed):
        self.name = name
        self.color = color
        self.actions = []
        self.reactions = []
        self.effects = []
        self.skills = []
        self.immunities = []
        self.atk = attack
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
