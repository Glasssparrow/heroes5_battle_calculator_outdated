from keywords import *


class Melee:

    def __init__(self, owner):
        self.owner = owner
        self.keyword = MELEE_ATTACK

    def act(self, target):
        print(f"{self.owner.name} атакует {target.name}")
