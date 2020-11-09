from classicwowsim.object import BasicWeapon
from classicwowsim.object.items.utils.constants import WeaponHand, WeaponType


class ClawOfTheBlackDrake(BasicWeapon):
    name = "Claw of the Black Drake"
    weapon_hand = WeaponHand.MAIN_HAND
    weapon_type = WeaponType.FIST
    damage_lower = 102
    damage_upper = 191
    speed = 2.60
    strength = 13
    critical = 1

