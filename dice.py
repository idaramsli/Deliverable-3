import random


class Dice:
    """
    A dice with n-sides, can be rolled for random values.
    """

    def __init__(self, sides: int = 6) -> None:
        """
        Make a dice with minimum 2-sides, default is 6-sides (like a normal dice).
        """
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides")
        self.sides = sides

    def roll(self) -> int:
        """Roll the dice and return a random number between 1 and the number of sides."""
        return random.randint(1, self.sides)

    def __call__(self) -> int:
        """
        Allow calling the dice object by name: d20() == d20.roll()
        """
        return self.roll()

    def __repr__(self) -> str:
        return f"Dice(sides={self.sides})"



    