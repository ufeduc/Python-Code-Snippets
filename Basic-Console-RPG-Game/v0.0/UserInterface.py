from Character import Character
from Shop import Shop
from Arena import Arena
import sys

class Interface:
    @classmethod
    def first_greetings(self):
        print("Wellcome to the FighterZone!!!")

    @classmethod
    def get_input(cls):
        cls.first_greetings()
        user_input = input("Log In(1) or Sign Up(2): ")
        if user_input.lower() == "log in" or user_input == "1":
            username = input("Username: ")
            password = input("Password: ")
            return Database(username, password, "Log In").log_in()
        elif user_input.lower() == "sign up" or user_input == "2":
            username = input("Username: ")
            password = input("Password: ")
            return Database(username, password, "Sign Up").sign_up()
        else:
            return Interface.get_input()


    def __init__(self):
        pass

    def __repr__(self):
        return f"{self.username} {self.password}"

class Database(Interface):
    # @classmethod
    # def connect_database(cls):
    #     import sqlite3
    #     conn = sqlite3.connect("user.db")
    #     c = conn.cursor()
    database_counter = 0

    def __init__(self, username, password, text):
        self.username = username
        self.password = password
        self.text = text
        # super().__init__(username, password, text)
        # Database.database_counter += 1

    def __repr__(self):
        return f"{self.username} {username}"

    @property
    def database_counter(self):
        return Database.database_counter

    def log_in(self):
        import sqlite3
        conn = sqlite3.connect("user.db")
        c = conn.cursor()
        query = ''' SELECT * FROM Users WHERE username=? AND password=? '''
        c.execute(query, (self.username, self.password))
        result = c.fetchone()
        conn.commit()
        conn.close()
        if result:
            conn = sqlite3.connect("user.db")
            c = conn.cursor()
            query = ''' SELECT health, mana, attack, balance, experience, level, job
                        FROM Users WHERE username=? '''
            c.execute(query, (self.username,))
            health, mana, attack, balance, experience, level, job = c.fetchall()[0]
            # print(health, mana, attack, balance, job)
            conn.commit()
            conn.close()
            while True:
                action = input("Shop(1) Arena(2) Character(3) Exit(4) ")
                if action.lower() == "shop" or action == "1":
                    Shop(self.username, health, mana, attack, balance, job).buy()
                elif action.lower() == "arena" or action == "2":
                    Arena(self.username, health, mana, attack, balance, experience, level, job).arena()
                elif action.lower() == "character" or action == "3":
                    conn = sqlite3.connect("user.db")
                    c = conn.cursor()
                    query = ''' SELECT health, mana, attack, balance, experience, level, job
                                FROM Users WHERE username=? '''
                    c.execute(query, (self.username,))
                    health, mana, attack, balance, experience, level, job = c.fetchall()[0]
                    # print(health, mana, attack, balance, job)
                    conn.commit()
                    conn.close()
                    print("==========================================")
                    print(f"Character type: {job}")
                    print(f"Money You Have: {balance} Health: {health} Mana: {mana}")
                    print(f"Attack: {attack} Experience: {experience} Level: {level}")
                    print("==========================================")
                elif action.lower() == "exit" or action == "4":
                    sys.exit()
                else:
                    pass

        # return "Failed Login"

    def sign_up(self):
        import sqlite3
        conn = sqlite3.connect("user.db")
        c = conn.cursor()
        query_check = ''' SELECT * FROM Users WHERE username= ? '''
        c.execute(query_check, (self.username))
        result = c.fetchone()
        conn.commit()
        conn.close()
        if result:
            print("Character already exist!")
            sys.exit()
        else:
            conn = sqlite3.connect("user.db")
            c = conn.cursor()
            data = (self.username, self.password, None,
                    None, None, None, None, None, None)
            query = ''' INSERT INTO Users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            c.execute(query,data)
            conn.commit()
            conn.close()
            Character(self.username).create_character()
        return f"{self.username} Has Succesfully Signed Up!!!"



Interface().get_input()
