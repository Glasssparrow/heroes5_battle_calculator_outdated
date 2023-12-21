

class Skill:

    def __init__(self, owner):
        self.owner = owner
        self.name = "default"
        self.activation_cases = []


def calculate_base_chance(user, target):
    if user.hp > target.hp:
        return 0.25 + user.hp/target.hp
    else:
        return 0.25 - target.hp/user.hp
