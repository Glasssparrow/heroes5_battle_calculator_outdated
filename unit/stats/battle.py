from .common import Stat


class MinDamage(Stat):

    pass


class MaxDamage(Stat):

    pass


class Health(Stat):

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
