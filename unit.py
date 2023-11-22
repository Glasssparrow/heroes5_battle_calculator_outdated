

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

    def __init__(self):
        self.actions = []
        self.reactions = []
        self.effects = []
        self.skills = []
        self.immunities = []
