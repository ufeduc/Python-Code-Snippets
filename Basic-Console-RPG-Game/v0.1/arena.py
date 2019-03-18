class Arena:
    def __init__(self, username, health, mana, attack, balance, experience, level):
        self.username   = username
        self.health     = health
        self.mana       = mana
        self.attack     = attack
        self.balance    = balance
        self.experience = experience
        self.level      = level 

    @property
    def goblin(self):
        health     = 1000
        attack     = 1000
        experience = 50
        balance    = 2000
        return health, attack, experience, balance
    
    @property
    def orc(self):
        health     = 2000
        attack     = 2000
        experience = 25
        balance    = 4000
        return health, attack, experience, balance
    
    @property
    def uruk(self):
        health     = 3000
        attack     = 3000
        experience = 20
        balance    = 8000
        return health, attack, experience, balance

    def fight(self):
        if self.health <= 0:
            return "You should rest!"
        else:
            if self.level == 1:
                enemy_health, enemy_attack, enemy_experience, enemy_balance = self.goblin
                while enemy_health > 0 and self.health > 0:
                    move = input("Attack(1) Escape(any key): ")
                    if move.lower() == "attack" or move == '1':
                        if self.mana < 500:
                            enemy_health -= (self.attack*(0.1))
                        else:
                            enemy_health -= self.attack
                            self.mana    -= 500
                        self.health  -= enemy_attack
                        
                        print(f"Hero: {self.username} Health: {self.health} Mana: {self.mana}")
                        print(f"Enemy: Orc Health: {enemy_health}")
                    else:
                        break
                if enemy_health <= 0:
                    self.balance    += enemy_balance
                    self.experience += enemy_experience
                    if self.experience >= 100:
                        self.experience -= 100
                        self.level      += 1
                return self.health, self.mana, self.balance, self.experience, self.level

            elif self.level == 2:
                enemy_health, enemy_attack, enemy_experience, enemy_balance = self.orc
                while enemy_health > 0 and self.health > 0:
                    move = input("Attack(1) Escape(any key): ")
                    if move.lower() == "attack" or move == '1':
                        if self.mana < 500:
                            enemy_health -= (self.attack*(0.1))
                        else:
                            enemy_health -= self.attack
                            self.mana    -= 500
                        self.health  -= enemy_attack
                        
                        print(f"Hero: {self.username} Health: {self.health} Mana: {self.mana}")
                        print(f"Enemy: Orc Health: {enemy_health}")
                    else:
                        break
                if enemy_health <= 0:
                    self.balance    += enemy_balance
                    self.experience += enemy_experience
                    if self.experience >= 100:
                        self.experience -= 100
                        self.level      += 1
                return self.health, self.mana, self.balance, self.experience, self.level
            else:
                enemy_health, enemy_attack, enemy_experience, enemy_balance = self.uruk
                while enemy_health > 0 and self.health > 0:
                    move = input("Attack(1) Escape(any key): ")
                    if move.lower() == "attack" or move == '1':
                        if self.mana < 500:
                            enemy_health -= (self.attack*(0.1))
                        else:
                            enemy_health -= self.attack
                            self.mana    -= 500
                        self.health  -= enemy_attack
                        
                        print(f"Hero: {self.username} Health: {self.health} Mana: {self.mana}")
                        print(f"Enemy: Orc Health: {enemy_health}")
                    else:
                        break
                if enemy_health <= 0:
                    self.balance    += enemy_balance
                    self.experience += enemy_experience
                    if self.experience >= 100:
                        self.experience -= 100
                        self.level      += 1
                return self.health, self.mana, self.balance, self.experience, self.level

