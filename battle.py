from character import Character


class Battle:
    def __init__(self, hero: Character, enemy: Character) -> None:
        self.hero = hero
        self.enemy = enemy
        
    def play_round(self) -> None:
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)
        else:
            print(f"{self.enemy.name} has been defeated!")

    def simulate_battle(self) -> None:
        round_number = 1
        while self.hero.is_alive and self.enemy.is_alive:
            print(f"Round {round_number}:")
            self.play_round()
            round_number += 1
            
        if self.hero.is_alive:
            print(f"{self.hero.name} wins!")
        else:
            print(f"{self.enemy.name} wins!")