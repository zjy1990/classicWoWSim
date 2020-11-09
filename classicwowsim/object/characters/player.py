import numpy as np
from classicwowsim.object.characters.utils.constants import Races, Classes

class BasicPlayer(object):
    strength = 0
    agility = 0
    hit = 0
    critical = 0
    race = None
    wow_class = None
    main_skill = 300
    off_skill = 300

    @property
    def attack_power(self):
        return self.get_attack_power()

    @classmethod
    def get_attack_power(self):
        pass

    def __repr__(self):
        return f"""{self.race} {self.wow_class}:
                Strength: {self.strength}  
                Agility: {self.agility}
                Attack Power: {self.attack_power}
                Hit: {np.round(self.hit,2)}% 
                Critical Strike: {np.round(self.critical,2)}%
                Main Hand Skill: {self.main_skill}
                Off Hand Skill: {self.off_skill}
                """

class RogueOrc(BasicPlayer):
    race = Races.ORC
    wow_class = Classes.ROGUE
    strength = 83
    agility = 127
