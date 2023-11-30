from unit.unit import Unit
from keywords import *
from unit.actions.melee import *


peasant = Unit(
    name="Крестьянин", color="Синий",
    attack=1, defence=1, min_damage=1, max_damage=1,
    health=3, initiative=8, speed=4
)
knight = Unit(
    name="Рыцарь", color="Красный",
    attack=23, defence=21, min_damage=20, max_damage=30,
    health=90, initiative=11, speed=7
)
peasant.get_quantity(1)
knight.get_quantity(1)

peasant.add_action(Melee)
knight.add_action(Melee)

knight.take_action(MELEE_ATTACK, peasant)
