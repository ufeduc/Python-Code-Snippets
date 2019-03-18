class Shop:
    def __init__(self, balance, level, job):
        self.balance = balance
        self.level   = level
        self.job     = job.lower()

    def buy(self, item):
        if self.level < item['level']:
            print("You are not able to use it because of your level")
        else:
            if self.balance < item['price']:
                print("Your fund is not enough to afford this item")
            else:
                print(f"{item}")# this needs to be handle


    def items(self):
        from difflib import get_close_matches
        items_input = input("armor(1) weapon(2) potion(3) back(any key)")
        if items_input == "armor" or items_input == '1':
            for item in self.armor.keys():
                print(f"Item: {item} Level: {self.armor[item]['level']} Health: {self.armor[item]['health']} Price: {self.armor[item]['price']}")
            item = input("Choose one of them: ")
            if item in self.armor.keys():
                Shop(self.balance, self.level, self.job).buy(self.armor[item])
            else:
                print("Wrong Input")

        elif items_input == "weapon" or items_input == '2':
            for item in self.weapon.keys():
                print(f"Item: {item} Level: {self.weapon[item]['level']} Attack: {self.weapon[item]['attack']} Price: {self.weapon[item]['price']}")
            item = input("Choose one of them: ")
            if item in self.weapon.keys():
                Shop(self.balance, self.level, self.job).buy(self.weapon[item])
            else:
                print("Wrong Input")

        elif items_input == "potion" or items_input == '3':
            for item in self.potion.keys():
                print(f"Item: {item} Mana: {self.potion[item]['mana']} Price: {self.potion[item]['price']}")
            item = input("Choose one of them: ")
            if item in self.potion.keys():
                Shop(self.balance, self.level, self.job).buy(self.potion[item])
            else:
                print("Wrong Input")
        


    def interraction_with_shop(self):
        if self.job == "warrior":
            WarriorItem(self.balance, self.level, self.job).items()
        elif self.job == "assassin":
            AssassinItem(self.balance, self.level, self.job).items()
        else:
            MageItem(self.balance, self.level, self.job).items()


class WarriorItem(Shop):
    def __init__(self, balance, level, job):
        super().__init__(balance, level, job)
        self.armor  = {'chain':{'level':1, 'health':2000, 'price':1000},
                       'shell':{'level':2, 'health':5000, 'price':3000}}
        self.weapon = {'sword':{'level':1, 'attack':3000, 'price':2000},
                       'axe'  :{'level':2, 'attack':6000, 'price':4000}}
        self.potion = {'potion of warrior':{'level':1 ,'health':5000, 'mana':2000, 'price':1000}}

class AssassinItem(Shop):
    def __init__(self, balance, level, job):
        super().__init__(balance, level, job)
        self.armor  = {'leather':{'level':1, 'health':2000, 'price':1000},
                       'chitin':{'level':2, 'health':5000, 'price':3000}}
        self.weapon = {'dagger':{'level':1, 'attack':3000, 'price':2000},
                       'bow'  :{'level':2, 'attack':6000, 'price':4000}}
        self.potion = {'potion of assassin':{'level':1 ,'health':3000, 'mana':1000, 'price':1000}}

class MageItem(Shop):
    def __init__(self, balance, level, job):
        super().__init__(balance, level, job)
        self.armor  = {'cloth':{'level':1, 'health':2000, 'price':1000},
                       'cloak':{'level':2, 'health':5000, 'price':3000}}
        self.weapon = {'wand':{'level':1, 'attack':3000, 'price':2000},
                       'staff'  :{'level':2, 'attack':6000, 'price':4000}}
        self.potion = {'potion of mage':{'level':1 ,'health':5000, 'mana':2000, 'price':1000}}

