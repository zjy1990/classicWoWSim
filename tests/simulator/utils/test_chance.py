import unittest
import numpy as np
from classicwowsim.simulator.utils.chance import calc_miss_chance



class TestChance(unittest.TestCase):


    def test_calc_miss_chance_normal_305(self):
        base_hit = 0.06
        target_level = 63
        attack_skill = 305
        dual_wield = False
        miss_chance = calc_miss_chance(base_hit,attack_skill, target_level, dual_wield)
        desired_miss_chance = 0.00
        np.isclose(miss_chance,desired_miss_chance, rtol= 10**-3)

    def test_calc_miss_chance_normal_300(self):
        base_hit = 0.06
        target_level = 63
        attack_skill = 300
        dual_wield = False
        miss_chance = calc_miss_chance(base_hit,attack_skill, target_level, dual_wield)
        desired_miss_chance = 0.03
        np.isclose(miss_chance,desired_miss_chance, rtol= 10**-3)

    def test_calc_miss_chance_normal_308(self):
        base_hit = 0.00
        target_level = 63
        attack_skill = 308
        dual_wield = False
        miss_chance = calc_miss_chance(base_hit,attack_skill, target_level, dual_wield)
        desired_miss_chance = 0.057
        np.isclose(miss_chance,desired_miss_chance, rtol= 10**-3)

    def test_calc_miss_chance_normal_312(self):
        base_hit = 0.00
        target_level = 63
        attack_skill = 312
        dual_wield = False
        miss_chance = calc_miss_chance(base_hit,attack_skill, target_level, dual_wield)
        desired_miss_chance = 0.053
        np.isclose(miss_chance,desired_miss_chance, rtol= 10**-3)


    def test_calc_miss_chance_dual_weild_305(self):
        base_hit = 0.09
        target_level = 63
        attack_skill = 305
        dual_wield = True
        miss_chance = calc_miss_chance(base_hit,attack_skill, target_level, dual_wield)
        desired_miss_chance = 0.158
        np.isclose(miss_chance,desired_miss_chance, rtol= 10**-3)
