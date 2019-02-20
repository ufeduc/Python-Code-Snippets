class Shop:
    def __init__(self, username, health, mana, attack, balance, job):
        self.username = username
        self.mana     = mana
        self.health   = health
        self.attack   = attack
        self.balance  = balance
        self.job      = job

    def buy(self):
        print("======================")
        print("Wellcome To The Armory")
        print("======================")
        equipment = input("Arm(1) Armor(2) Potion(3) Back(4): ")
        if equipment.lower() == "arm" or equipment == '1':
            weapon = input("Dagger(1) Staff(2) Axe(3) Back(4): ")
            if weapon.lower() == "dagger" or weapon == '1':
                Arm(self.username, self.health, self.mana,\
                    self.attack, self.balance, self.job).Dagger()
            elif weapon.lower() == "staff" or weapon == '2':
                Arm(self.username, self.health, self.mana,\
                    self.attack, self.balance, self.job).Staff()
            elif weapon.lower() == "axe" or weapon == '3':
                Arm(self.username, self.health, self.mana,\
                    self.attack, self.balance, self.job).Axe()
            else:
                pass
        elif equipment.lower() == "armor" or equipment == '2':
            armor = input("Leather(1) Cloth(2) Chain(3) Back(4) ")
            if armor.lower() == "leather" or armor == "1":
                Armor(self.username, self.health, self.mana,\
                    self.attack, self.balance, self.job).Leather()
            elif armor.lower() == "cloth" or armor == "2":
                Armor(self.username, self.health, self.mana,\
                    self.attack, self.balance, self.job).Cloth()
            elif armor.lower() == "chain" or armor == "3":
                Armor(self.username, self.health, self.mana,\
                    self.attack, self.balance, self.job).Chain()
            else:
                pass
        elif equipment.lower() == "potion" or equipment == '3':
            potion = input("Health Potion(1) Mana Potion(2) Back(3) ")
            if potion.lower() == "health" or potion == "1":
                Potion(self.username, self.health, self.mana,\
                    self.attack, self.balance, self.job).HealthPotion()
            elif potion.lower() == "mana" or potion == "2":
                Potion(self.username, self.health, self.mana,\
                    self.attack, self.balance, self.job).ManaPotion()
            else:
                pass
        elif equipment.lower() == "exit" or equipment == '4':
            pass
        else:
            pass


class Arm(Shop):
    def __init__(self, username, health, mana, attack, balance, job):
        super().__init__(username, health, mana, attack, balance, job)

    @property
    def dagger_price(self): return 1000
    @property
    def dagger_damage(self):return 1000
    def Dagger(self):
        if self.job == "ASSASSIN":
            if self.balance >= self.dagger_price:
                self.balance -= self.dagger_price
                self.attack  += self.dagger_damage
                import sqlite3
                conn = sqlite3.connect("user.db")
                c = conn.cursor()
                data = (self.balance, self.attack, self.username)
                query = ''' UPDATE Users SET balance= ?, attack= ? WHERE username= ? '''
                c.execute(query, data)
                conn.commit()
                conn.close()
                print(f"Attack is {self.attack} Balance is {self.balance}")
            else:
                print(f"You Dont Have Enough Money To Afford Dagger. Current Money: {self.balance}")
                return Shop(self.username, self.health, self.mana, self.attack, self.balance, self.job).buy()
        else:
            print(f"You Are Not Fit To Use Dagger! You Are a/an {self.job} MAN!!!")
            return Shop(self.username, self.health, self.mana, self.attack, self.balance, self.job).buy()


    @property
    def staff_price(self): return 1000
    @property
    def staff_damage(self):return 1000
    def Staff(self):
        if self.job == "MAGICIAN":
            if self.balance >= self.staff_price:
                self.balance -= self.staff_price
                self.attack  += self.staff_damage
                import sqlite3
                conn = sqlite3.connect("user.db")
                c = conn.cursor()
                data = (self.balance, self.attack, self.username)
                query = ''' UPDATE Users SET balance= ?, attack= ? WHERE username= ? '''
                c.execute(query, data)
                conn.commit()
                conn.close()
                print(f"Attack is {self.attack} Balance is {self.balance}")
            else:
                print(f"You Dont Have Enough Money To Afford Staff. Current Money: {self.balance}")
                return Shop(self.username, self.health, self.mana, self.attack, self.balance, self.job).buy()
        else:
            print(f"You Are Not Fit To Use Staff! You Are a/an {self.job} MAN!!!")
            return Shop(self.username, self.health, self.mana, self.attack, self.balance, self.job).buy()

    @property
    def axe_price(self): return 1000
    @property
    def axe_damage(self):return 1000
    def Axe(self):
        if self.job == "WARRIOR":
            if self.balance >= self.axe_price:
                self.balance -= self.axe_price
                self.attack  += self.axe_damage
                import sqlite3
                conn = sqlite3.connect("user.db")
                c = conn.cursor()
                data = (self.balance, self.attack, self.username)
                query = ''' UPDATE Users SET balance= ?, attack= ? WHERE username= ? '''
                c.execute(query, data)
                conn.commit()
                conn.close()
                print(f"Attack is {self.attack} Balance is {self.balance}")
            else:
                print(f"You Dont Have Enough Money To Afford Axe. Current Money: {self.balance}")
                return Shop(self.username, self.health, self.mana, self.attack, self.balance, self.job).buy()
        else:
            print(f"You Are Not Fit To Use Axe! You Are a/an {self.job} MAN!!!")
            return Shop(self.username, self.health, self.mana, self.attack, self.balance, self.job).buy()



class Armor(Shop):
    def __init__(self, username, health, mana, attack, balance, job):
        super().__init__(username, health, mana, attack, balance, job)

    @property
    def leather_price(self): return 1000
    @property
    def leather_health(self):return 1000
    def Leather(self):
        if self.job == "ASSASSIN":
            if self.balance >= self.leather_price:
                self.balance -= self.leather_price
                self.health  += self.leather_health
                import sqlite3
                conn = sqlite3.connect("user.db")
                c = conn.cursor()
                data = (self.balance, self.health, self.username)
                query = ''' UPDATE Users SET balance= ?, attack= ? WHERE username= ? '''
                c.execute(query, data)
                conn.commit()
                conn.close()
                print(f"Health is {self.health} Balance is {self.balance}")
            else:
                print(f"You Dont Have Enough Money To Afford Leather. Current Money: {self.balance}")
                return Shop(self.username, self.health, self.mana, self.attack, self.balance, self.job).buy()
        else:
            print(f"You Are Not Fit To Use Leather! You Are a/an {self.job} MAN!!!")
            return Shop(self.username, self.health, self.mana, self.attack, self.balance, self.job).buy()


    @property
    def cloth_price(self): return 1000
    @property
    def cloth_health(self):return 1000
    def Cloth(self):
        if self.job == "MAGICIAN":
            if self.balance >= self.cloth_price:
                self.balance -= self.cloth_price
                self.health  += self.cloth_health
                import sqlite3
                conn = sqlite3.connect("user.db")
                c = conn.cursor()
                data = (self.balance, self.health, self.username)
                query = ''' UPDATE Users SET balance= ?, health= ? WHERE username= ? '''
                c.execute(query, data)
                conn.commit()
                conn.close()
                print(f"Health is {self.health} Balance is {self.balance}")
            else:
                print(f"You Dont Have Enough Money To Afford Cloth. Current Money: {self.balance}")
                return Shop(self.username, self.health, self.mana, self.attack, self.balance, self.job).buy()
        else:
            print(f"You Are Not Fit To Use Cloth! You Are a/an {self.job} MAN!!!")
            return Shop(self.username, self.health, self.mana, self.attack, self.balance, self.job).buy()

    @property
    def chain_price(self): return 1000
    @property
    def chain_health(self):return 1000
    def Chain(self):
        if self.job == "WARRIOR":
            if self.balance >= self.chain_price:
                self.balance -= self.chain_price
                self.health  += self.chain_health
                import sqlite3
                conn = sqlite3.connect("user.db")
                c = conn.cursor()
                data = (self.balance, self.health, self.username)
                query = ''' UPDATE Users SET balance= ?, health= ? WHERE username= ? '''
                c.execute(query, data)
                conn.commit()
                conn.close()
                print(f"Health is {self.health} Balance is {self.balance}")
            else:
                print(f"You Dont Have Enough Money To Afford Chain. Current Money: {self.balance}")
                return Shop(self.username, self.health, self.mana, self.attack, self.balance, self.job).buy()
        else:
            print(f"You Are Not Fit To Use Chain! You Are a/an {self.job} MAN!!!")
            return Shop(self.username, self.health, self.mana, self.attack, self.balance, self.job).buy()

class Potion(Shop):
    def __init__(self, username, health, mana, attack, balance, job):
        super().__init__(username, health, mana, attack, balance, job)

    @property
    def health_price(self): return 1000
    @property
    def health_potion(self):return 1000
    def HealthPotion(self):
        if self.balance >= self.health_price:
            self.balance -= self.health_price
            self.health  += self.health_potion
            import sqlite3
            conn = sqlite3.connect("user.db")
            c = conn.cursor()
            data = (self.balance, self.health, self.username)
            query = ''' UPDATE Users SET balance= ?, health= ? WHERE username= ? '''
            c.execute(query, data)
            conn.commit()
            conn.close()
            print(f"Health is {self.health} Balance is {self.balance}")
        else:
            print(f"You Dont Have Enough Money To Afford Health Potion. Current Money: {self.balance}")
            return Shop(self.username, self.health, self.mana, self.attack, self.balance, self.job).buy()



    @property
    def mana_price(self): return 1000
    @property
    def mana_potion(self):return 1000
    def ManaPotion(self):
        if self.balance >= self.mana_price:
            self.balance -= self.mana_price
            self.mana  += self.mana_potion
            import sqlite3
            conn = sqlite3.connect("user.db")
            c = conn.cursor()
            data = (self.balance, self.mana, self.username)
            query = ''' UPDATE Users SET balance= ?, mana= ? WHERE username= ? '''
            c.execute(query, data)
            conn.commit()
            conn.close()
            print(f"Mana is {self.mana} Balance is {self.balance}")
        else:
            print(f"You Dont Have Enough Money To Afford Mana Potion. Current Money: {self.balance}")
            return Shop(self.username, self.health, self.mana, self.attack, self.balance, self.job).buy()
