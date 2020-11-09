import numpy as np

class BasicItem(object):
    name = None
    strength = 0
    agility = 0
    hit = 0
    critical = 0
    attack_power = 0
    skill = 0
    skill_type = None
    set = None

    def __repr__(self):
        return f"""{self.name}:
                +{self.strength} Strength 
                +{self.agility} Agility
                +{self.attack_power} Attack Power
                +{self.hit}% chance to hit
                +{self.critical}% chance to critical strike
                +{self.skill} {self.skill_type} skill
                set: {self.set}
                """


class BasicWeapon(object):
    name = None
    weapon_type = None
    weapon_hand = None
    damage_lower = 0
    damage_upper = 0
    speed = 1.0
    strength = 0
    agility = 0
    hit = 0
    critical = 0
    attack_power = 0
    skill = 0
    set = None

    @property
    def dps(self):
        return (self.damage_lower + self.damage_upper) * 0.5 / self.speed

    def __repr__(self):
        return f"""{self.name}:
                {self.weapon_hand} {self.weapon_type} 
                {self.damage_lower} - {self.damage_upper} Damage
                speed {np.round(self.speed,2)}
                {np.round(self.dps,1)} damage per second
                +{self.strength} Strength 
                +{self.agility} Agility
                +{self.attack_power} Attack Power
                +{self.hit}% chance to hit
                +{self.critical}% chance to critical strike
                +{self.skill} {self.weapon_type} skill
                set: {self.set}
                """
