


def calc_miss_chance(base_hit = 0.06, attack_skill=300, target_level=63, dual_wield=True):
    target_skill = target_level * 5
    if target_skill - attack_skill >= 11:
        miss_chance = 0.05 + (target_skill - attack_skill) * 0.002
    else:
        miss_chance = 0.05 + (target_skill - attack_skill) * 0.001

    if dual_wield:
        miss_chance = miss_chance * 0.8 + 0.2
    return max(miss_chance - base_hit, 0)

def calc_glancing_chance(attack_level=60, target_level=63):
    glancing_chance = 0.1 + (target_level * 5 - attack_level *5 ) * 0.02
    return glancing_chance

def calc_glancing_lower_upper(attack_skill=300, target_level=63):
    lower = min(1.3 - 0.05 * (target_level * 5 - attack_skill), 0.91)
    upper = min(1.2 - 0.03 * (target_level * 5 - attack_skill), 0.99)
    return lower, upper

def calc_dodge_chance(attack_skill=300, target_level=63):
    dodge_chance = 0.05 + (target_level *5 - attack_skill) * 0.001
    return dodge_chance

def calc_critical_chance(base_critical = 0.05, attack_level=60, target_level=63):
    attack_skill = attack_level * 5
    target_skill = target_level * 5
    if attack_skill - target_skill < 0:
        critical_chance = base_critical + (attack_skill - target_skill) * 0.002
    else:
        critical_chance = base_critical + (attack_skill - target_skill) * 0.0004
    return critical_chance

