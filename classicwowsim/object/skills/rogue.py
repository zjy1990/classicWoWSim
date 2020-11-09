


class RogueSkillBase(object):
    name = None
    rank = 1
    energy = 0
    cooldown = 0

class FinishSkillDamage(object):
    def __init__(self, combo_point, lower, upper):
        self.combo_point = combo_point
        self.lower = lower
        self.upper = upper

class SinisterStrike(RogueSkillBase):
    name = 'Sinister Strike'
    _energy = 45
    rank = 8
    bonus_damage = 68
    combo_point_award = 1
    def __init__(self, weapon_damage, improved=True):
        self.base_damange = weapon_damage
        self.improved = improved

    @property
    def energy(self):
        return self._energy - 5 if self.improved else self._energy

    @property
    def damage(self):
        return self.base_damange + self.bonus_damage


class Eviscerate(RogueSkillBase):
    name = 'Eviscerate'
    energy = 35
    rank = 8
    base_damage = []
    base_damage.append(FinishSkillDamage(1, 199, 295))
    base_damage.append(FinishSkillDamage(2, 350, 446))
    base_damage.append(FinishSkillDamage(3, 501, 597))
    base_damage.append(FinishSkillDamage(4, 652, 748))
    base_damage.append(FinishSkillDamage(5, 803, 899))

    def __init__(self, aggression=True, improved=True, deathdealer=True):
        self.aggression = aggression
        self.improved = improved
        self.deathdealer = deathdealer

