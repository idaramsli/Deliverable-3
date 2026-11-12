from dice import Dice


class Weapon:

    # Defines the weapon with a name and damage dice
    def __init__(self, name: str, damage_dice: Dice) -> None:
        self.name = name
        self.damage_dice = damage_dice

    # Returns the damage rolled by the dice
    def roll_damage(self) -> int:
        return self.damage_dice.roll()