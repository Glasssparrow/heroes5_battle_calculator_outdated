

class Skill:

    def __init__(self, owner):
        self.owner = owner
        self.name = "default"
        self.activation_cases = []


def calculate_base_chance(user, target):
    if user.hp > target.hp:
        chance = 0.25 + 0.03 * user.hp/target.hp
    else:
        chance = 0.25 - 0.03 * target.hp/user.hp
    if chance < 0.05:
        return 0.05
    elif chance > 0.75:
        return 0.75
    else:
        return chance
