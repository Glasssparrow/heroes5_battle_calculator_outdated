from random import random


class Skill:

    def __init__(self, owner):
        self.owner = owner
        self.name = "default"
        self.keyword = "no keyword"


def check_random(chance):
    if not isinstance(chance, (int, float)):
        raise Exception(
            "Не верный тип данных"
        )
    if chance < 0 or chance > 1:
        raise Exception(
            "Не в промежутке 0 < chance < 1"
        )
    if chance < random():
        return True
    else:
        return False

