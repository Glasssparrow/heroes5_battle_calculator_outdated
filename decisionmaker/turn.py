from .decisionmaker import DecisionMaker


# Для принятия решения нужно:
# 1) Список доступных для передвижения ячеек
# 2) Список доступных действий
# 3) Зона рукопашной атаки противника.
# 4) Список навыков врагов и их координаты
# 6) Список доступных ячеек с которых можно ударить.
# 7) Список доступных ячеек с возможностью ударить на следующий ход.
# 8) Расстояния от доступных ячеек до ближайшего врага.
def act(active_unit, battle_map):
    available_cells = battle_map.get_available_cells(active_unit)
    for coord, length, path in available_cells:
        pass
    actions_available = active_unit.actions
    enemy_units = {}
    enemy_danger_zones = {}
    for unit in battle_map.units:
        if unit.side == active_unit.side:
            continue
        enemy_units[unit.id] = unit
        enemy_danger_zones[unit.id] = (
            battle_map.get_available_cells(active_unit)
        )
