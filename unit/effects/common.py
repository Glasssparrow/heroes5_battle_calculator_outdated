

class Effect:

    def __init__(self):
        self.name = "default"
        self.attack = 0
        self.defence = 0
        self.min_damage = 0
        self.max_damage = 0
        self.initiative = 0
        self.speed = 0
        self.luck = 0
        self.morale = 0
        self.time = 0
        self.initiative_mark = None
        self.special_effects = []
        self.dispell_conditions = []

    def reapply(self, new_instance):
        self.time = new_instance.time
