class Character:
    def __init__(self, username, balance = 4000, experience = 0, level = 1):
        self.username = username
        self.balance = balance
        self.experience = experience
        self.level = level
    def create_character(self):
        job = input("Character Choice: Warrior(1) Magician(2) Assassin(3): ")
        if job.lower() == "warrior" or job == '1':
            Warrior(self.username, self.balance, self.experience, self.level).create_warior()
        elif job.lower() == "magician" or job == '2':
            Magician(self.username, self.balance, self.experience, self.level).create_magician()
        elif job.lower() == "assassin" or job == '3':
            Assassin(self.username, self.balance, self.experience, self.level).create_assassin()
        else:
            return Character(self.username).create_character()



class Warrior(Character):
    def __init__(self, username, balance, experience, level):
        super().__init__(username, balance, experience, level)
        self.health = 9999
        self.mana = 2000
        self.physical = 1000
        self.job = "WARRIOR"

    def __repr__(self):
        return f"{self.username} {self.health} {self.mana} {self.physical}"

    def create_warior(self):
        import sqlite3
        conn = sqlite3.connect("user.db")
        c = conn.cursor()
        data = (self.health, self.mana, self.physical, self.balance,
                self.experience, self.level, self.job, self.username)
        query = ''' UPDATE Users SET health= ?, mana= ?,
                    attack= ?, balance= ?,experience= ?,
                    level= ?, job= ? WHERE username= ? '''
        c.execute(query, data)
        conn.commit()
        conn.close()

    def skill_one(self):
        pass
    def skill_one(self):
        pass
    def skill_one(self):
        pass


class Magician(Character):
    def __init__(self, username, balance, experience, level):
        super().__init__(username, balance, experience, level)
        self.health = 4000
        self.mana = 9999
        self.magic = 3000
        self.job = "MAGICIAN"

    def __repr__(self):
        return f"{self.username} {self.health} {self.mana} {self.magic}"

    def create_magician(self):
        import sqlite3
        conn = sqlite3.connect("user.db")
        c = conn.cursor()
        data = (self.health, self.mana, self.physical, self.balance,
                self.experience, self.level, self.job, self.username)
        query = ''' UPDATE Users SET health= ?, mana= ?,
                    attack= ?, balance= ?,experience= ?,
                    level= ?, job= ? WHERE username= ? '''
        c.execute(query, data)
        conn.commit()
        conn.close()

    def skill_one(self):
        pass
    def skill_one(self):
        pass
    def skill_one(self):
        pass


class Assassin(Character):
    def __init__(self, username, balance, experience, level):
        super().__init__(username, balance, experience, level)
        self.health = 6000
        self.mana = 2000
        self.physical = 2000
        self.job = "ASSASSIN"

    def __repr__(self):
        return f"{self.username} {self.health} {self.mana} {self.physical}"

    def create_assassin(self):
        import sqlite3
        conn = sqlite3.connect("user.db")
        c = conn.cursor()
        data = (self.health, self.mana, self.physical, self.balance,
                self.experience, self.level, self.job, self.username)
        query = ''' UPDATE Users SET health= ?, mana= ?,
                    attack= ?, balance= ?,experience= ?,
                    level= ?, job= ? WHERE username= ? '''
        c.execute(query, data)
        conn.commit()
        conn.close()

    def skill_one(self):
        pass
    def skill_one(self):
        pass
    def skill_one(self):
        pass



# c = Warrior("Tyran", 1000, 200, 500)
# print(c)
