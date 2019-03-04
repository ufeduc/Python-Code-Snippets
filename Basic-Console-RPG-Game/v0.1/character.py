class Character:
    def __init__(self, job):
        self.job        = job
        self.warrior    = ["warrior", '1']
        self.assassin   = ["assassin", '2']
        self.mage       = ["mage", '3']
        self.balance    = 2000
        self.experience = 0
        self.level      = 1

    def interraction_with_character_class(self):
        from difflib import get_close_matches
        if get_close_matches(self.job, self.warrior):
            return Warrior(self.balance, self.experience, self.level).properties()
        elif get_close_matches(self.job, self.assassin):
            return Assassin(self.balance, self.experience, self.level).properties()
        elif get_close_matches(self.job, self.mage):
            return Mage(self.balance, self.experience, self.level).properties()
        else:
            import sys # bug
            sys.exit() # bug

class Warrior(Character):
    def __init__(self, balance, experience, level):
        self.health     = 10000
        self.mana       = 4000
        self.attack     = 7000
        self.balance    = balance
        self.experience = experience
        self.level      = level
        self.job        = "Warrior"

    def __repr__(self):
        return f"Health: {self.health} Mana: {self.mana} Attack: {self.attack} Balance: {self.balance} Experience: {self.experience} Level: {self.level} Job: {self.job}"

    def properties(self):
        return self.health, self.mana, self.attack, self.balance, self.experience, self.level, self.job

class Assassin(Character):
    def __init__(self, balance, experience, level):
        self.health     = 7000
        self.mana       = 2000
        self.attack     = 5000
        self.balance    = balance
        self.experience = experience
        self.level      = level
        self.job        = "Assassin"

    def __repr__(self):
        return f"Health: {self.health} Mana: {self.mana} Attack: {self.attack} Balance: {self.balance} Experience: {self.experience} Level: {self.level} Job: {self.job}"

    def properties(self):
        return self.health, self.mana, self.attack, self.balance, self.experience, self.level, self.job

class Mage(Character):
    def __init__(self, balance, experience, level):
        self.health     = 4000
        self.mana       = 6000
        self.attack     = 10000
        self.balance    = balance
        self.experience = experience
        self.level      = level
        self.job        = "Mage"

    def __repr__(self):
        return f"Health: {self.health} Mana: {self.mana} Attack: {self.attack} Balance: {self.balance} Experience: {self.experience} Level: {self.level} Job: {self.job}"

    def properties(self):
        return self.health, self.mana, self.attack, self.balance, self.experience, self.level, self.job
