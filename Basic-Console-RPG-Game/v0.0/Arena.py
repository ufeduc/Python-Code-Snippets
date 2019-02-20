class Arena:
    def __init__(self, username, health, mana, attack, balance, experience, level, job):
        self.username   = username
        self.health     = health
        self.mana       = mana
        self.attack     = attack
        self.balance    = balance
        self.experience = experience
        self.level      = (level)
        self.job        = job

    def arena(self):
        if self.level == 1:
            LevelOne(self.username, self.health, self.mana, self.attack, self.balance, self.experience, self.level, self.job).fight()
        if self.level == 2:
            LevelTwo(self.username, self.health, self.mana, self.attack, self.balance, self.experience, self.level, self.job).fight()
        if self.level >= 3:
            LevelThree(self.username, self.health, self.mana, self.attack, self.balance, self.experience, self.level, self.job).fight()



class LevelOne(Arena):
    def __init__(self, username, health, mana, attack, balance, experience, level, job):
        super().__init__(username, health, mana, attack, balance, experience, level, job)

    @property
    def goblin(self):
        attack = 1000
        health = 10000
        experience = 50
        balance = 2000
        return attack, health, experience, balance

    def fight(self):
        print("Enemy is a Goblin!!!")
        attack, health, experience, balance = self.goblin
        while True:
            print(f"{self.username} health is {self.health}")
            print(f"Goblins health is {health}")
            action = input("Attack(1) Escape(2) ")
            if action.lower() == "attack" or action == '1':
                self.health -= attack
                health -= self.attack
                if health <= 0:
                    print("well done you killed the goblins!!!")
                    print(f"reward is exp: {experience} money: {balance}")
                    self.experience += experience
                    self.balance += balance
                    if self.experience >= 100:
                        self.experience = 0
                        self.level += 1

                    import sqlite3
                    conn = sqlite3.connect("user.db")
                    c = conn.cursor()
                    data = (self.health, self.experience, self.level, self.balance, self.username)
                    query = ''' UPDATE  Users SET health= ?, experience= ?, level= ?, balance= ?
                                WHERE username= ? '''
                    c.execute(query, data)
                    conn.commit()
                    conn.close()
                    break
                if self.health <= 0:
                    print("you are dead!")
                    import sqlite3
                    conn = sqlite3.connect("user.db")
                    c = conn.cursor()
                    data = (self.health)
                    query = ''' UPDATE  Users SET health= ?
                                WHERE username= ? '''
                    c.execute(query, data)
                    conn.commit()
                    conn.close()
                    break


            elif action.lower() == "escape" or action == '2':
                break
            else:
                pass

class LevelTwo(Arena):
    def __init__(self, username, health, mana, attack, balance, experience, level, job):
        super().__init__(username, health, mana, attack, balance, experience, level, job)

    @property
    def orc(self):
        attack = 2000
        health = 10000
        experience = 75
        balance = 2000
        return attack, health, experience, balance

    def fight(self):
        print("Enemy is a orc!!!")
        attack, health, experience, balance = self.orc
        while True:
            print(f"{self.username} health is {self.health}")
            print(f"orcs health is {health}")
            action = input("Attack(1) Escape(2) ")
            if action.lower() == "attack" or action == '1':
                self.health -= attack
                health -= self.attack
                if health <= 0:
                    print("well done you killed the orcs!!!")
                    print(f"reward is exp: {experience} money: {balance}")
                    self.experience += experience
                    self.balance += balance
                    if self.experience >= 100:
                        self.experience = 0
                        self.level += 1

                    import sqlite3
                    conn = sqlite3.connect("user.db")
                    c = conn.cursor()
                    data = (self.health, self.experience, self.level, self.balance, self.username)
                    query = ''' UPDATE  Users SET health= ?, experience= ?, level= ?, balance= ?
                                WHERE username= ? '''
                    c.execute(query, data)
                    conn.commit()
                    conn.close()
                    break
                if self.health <= 0:
                    print("you are dead!")
                    import sqlite3
                    conn = sqlite3.connect("user.db")
                    c = conn.cursor()
                    data = (self.health)
                    query = ''' UPDATE  Users SET health= ?
                                WHERE username= ? '''
                    c.execute(query, data)
                    conn.commit()
                    conn.close()
                    break


            elif action.lower() == "escape" or action == '2':
                break
            else:
                pass


class LevelThree(Arena):
    def __init__(self, username, health, mana, attack, balance, experience, level, job):
        super().__init__(username, health, mana, attack, balance, experience, level, job)

    @property
    def uruk(self):
        attack = 3000
        health = 10000
        experience = 100
        balance = 2000
        return attack, health, experience, balance

    def fight(self):
        print("Enemy is a uruk!!!")
        attack, health, experience, balance = self.uruk
        while True:
            print(f"{self.username} health is {self.health}")
            print(f"uruks health is {health}")
            action = input("Attack(1) Escape(2) ")
            if action.lower() == "attack" or action == '1':
                self.health -= attack
                health -= self.attack
                if health <= 0:
                    print("well done you killed the uruks!!!")
                    print(f"reward is exp: {experience} money: {balance}")
                    self.experience += experience
                    self.balance += balance
                    if self.experience >= 100:
                        self.experience = 0
                        self.level += 1

                    import sqlite3
                    conn = sqlite3.connect("user.db")
                    c = conn.cursor()
                    data = (self.health, self.experience, self.level, self.balance, self.username)
                    query = ''' UPDATE  Users SET health= ?, experience= ?, level= ?, balance= ?
                                WHERE username= ? '''
                    c.execute(query, data)
                    conn.commit()
                    conn.close()
                    break
                if self.health <= 0:
                    print("you are dead!")
                    import sqlite3
                    conn = sqlite3.connect("user.db")
                    c = conn.cursor()
                    data = (self.health)
                    query = ''' UPDATE  Users SET health= ?
                                WHERE username= ? '''
                    c.execute(query, data)
                    conn.commit()
                    conn.close()
                    break
            elif action.lower() == "escape" or action == '2':
                break
            else:
                pass
