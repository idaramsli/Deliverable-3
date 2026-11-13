
class Character:
    def __init__(
            self, 
            name: str, 
            hp_max: int = 100,
            damage: int = 10,
            weapon=None
        ) -> None:
       
        """
        Initialise the Character with a name, maximum hit points (hp_max),
        damage value and an optional weapon.
        """
        self.name = name
        self._hp = hp_max  
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def take_damage(self, amount: int) -> None:
        """Reduce own HP by amount. HP cannot go below 0."""
        if amount < 0:
            raise ValueError("Damage can not be below 0")
        self._hp = max(self._hp - amount, 0)

    def heal(self, amount: int) -> None:
        """Increase own HP by amount. HP cannot exceed hp_max."""
        if amount < 0:
            raise ValueError("Heal amount can not be below 0")
        self._hp = min(self._hp + amount, self.hp_max)

    def attack(self, target: "Character") -> None:
        """Attacking target by using weapon damage or default damage if no weapon is equipped."""
        if self.weapon is not None:
            damage = self.weapon.roll_damage()
        else:
            damage = self.damage
        target.take_damage(damage)

    def introduce(self) -> None:
        """Print a introduction of the character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character, for user"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character, for programmer"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only: only possible to inspect HP."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Read-only: True if HP is over 0, if below 0 then False"""
        return self._hp > 0


class Warrior(Character):
    def __init__(
            self,
            name: str,
            hp_max: int = 100,
            damage: int = 10,
            weapon=None,
            armor: int = 5
    ) -> None:
        """
        Initialise the Warrior with a name, maximum hit points (hp_max),
        damage value, an optional weapon, and armor.
        """
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor

    def take_damage(self, amount: int) -> None:
        """Reduce incoming damage by armor value"""
        reduced_damage = max(amount - self.armor, 0)
        super().take_damage(reduced_damage)




class Mage(Character):
    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon=None,
        mana: int = 30,
        mana_max: int = 30
    ) -> None:

        """Initialise a Mage with mana."""
        super().__init__(name, hp_max, damage, weapon)
        self.mana_max = mana_max
        self.mana = min(mana, mana_max)

    def attack(self, target: "Character") -> None:
        """Use a magical attack if enough mana is available."""

        if self.mana >= 10:
            self.mana -= 10
            magic_damage = self.damage * 2
            target.take_damage(magic_damage)

        else:
            super().attack(target)
            self.mana = min(self.mana + 5, self.mana_max)