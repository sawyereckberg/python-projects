
class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health_amount):
        if health_amount < 0:
            self._health = 0
        if health_amount > 100:
            self._health = 100
        if health_amount <= 100 and health_amount >= 0:
            self._health = health_amount

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, mana_amount):
        if mana_amount < 0:
            self._mana = 0
        if mana_amount > 50:
            self._mana = 50
        if mana_amount <= 50 and mana_amount >= 0:
            self._mana = mana_amount

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f'{self.name} leveled up to {self._level}!')

    def __str__(self):
        return "Name: " + self.name + "\n" + "Level: " + str(self._level) + "\n" + "Health: " + str(self._health) + "\n" + "Mana: " + str(self._mana)



hero = GameCharacter('Kratos') # Creates a new character named Kratos
print(hero)  # Displays the character's stats

hero.health -= 30  # Decreases health by 30
hero.mana -= 10    # Decreases mana by 10
print(hero)  # Displays the updated stats

hero.level_up()  # Levels up the character
print(hero)  # Displays the stats after leveling up
    

    