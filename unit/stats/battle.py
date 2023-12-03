from .common import Stat
from math import floor


class MinDamage(Stat):

    def __get__(self, instance, owner):
        result = instance.__dict__[self.name]
        for buff in instance.__dict__["effects"]:
            result += buff.__dict__[self.stat]
        result = floor(result)
        if result < 0:
            return 0
        elif result < instance.__dict__["_min_damage_limit"]:
            return instance.__dict__["_min_damage_limit"]
        else:
            return result


class MaxDamage(Stat):

    def __get__(self, instance, owner):
        result = instance.__dict__[self.name]
        for buff in instance.__dict__["effects"]:
            result += buff.__dict__[self.stat]
        result = floor(result)
        if result < 0:
            return 0
        elif result > instance.__dict__["_max_damage_limit"]:
            return instance.__dict__["_max_damage_limit"]
        else:
            return result


class Health(Stat):

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
