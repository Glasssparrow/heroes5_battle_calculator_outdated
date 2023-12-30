from .common import Skill
from ..common import check_random
from ..effects import *
from keywords import *
from .apply_effect import PeasantBash
from ..requirements import push, run_away


class BearPush(PeasantBash):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "Удар лапой"
        self.activation_cases.append(ACTIVATE_AFTER_STRIKE)

    def use(self, target, damage, kills, battle_map):
        if (
            check_random(self.get_chance(target)) and
            not target.check_immunity(PUSH_IMMUNE)
        ):
            target.apply_effect(Bash())
            push(battle_map, self.owner, target)
        else:
            print(f"У {target.name} иммунитет к отталкиванию")

    def _chance_formula(self, base_chance):
        return 1-(1-base_chance)**self.owner.tiles_moved


class BearRoar(PeasantBash):

    def __init__(self, owner):
        super().__init__(owner)
        self.name = "Медвежий рёв"
        self.activation_cases.append(ACTIVATE_AFTER_STRIKE)

    def use(self, target, damage, kills, battle_map):
        if (
                check_random(self.get_chance(target)) and
                not target.check_immunity(FEAR_IMMUNE)
        ):
            target.apply_effect(Bash())
            run_away(battle_map, self.owner, target)
        else:
            print(f"У {target.name} иммунитет к запугиванию")

    def _chance_formula(self, base_chance):
        return 1 - (1 - base_chance) ** self.owner.tiles_moved
