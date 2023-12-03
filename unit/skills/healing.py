from .common import Skill
from keywords import *
from math import floor


class Vampire(Skill):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "Вампиризм"
        self.keyword = ACTIVATE_AFTER_STRIKE

    def use(self, target, damage, kills):
        amount_of_healing = floor(damage/2)
        revived = self.owner.take_healing(amount_of_healing)
        print(f"{self.owner.name} исцеляется на {amount_of_healing} "
              f"ударив {target.name}. "
              f"Возродилось {int(revived)} существ.")

