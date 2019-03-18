class Database:
    def __init__(self, username, password):
        self.data = []

    @property
    def connection_to_database(self):
        import pymysql.cursors
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='mysqlMYSQL321',
                                     cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        return cursor, connection

    def create_database(self):
        cursor, connection = self.connection_to_database
        try:
            for line in open('create_database.sql'):
                print(line)
                cursor.execute(line)

        except Exception as error_type:
            return f"{error_type}"
        finally:
            connection.commit()
            cursor.close()
            connection.close()

    @property
    def create_accounts(self, username, password):
        return username, password
    def update_accounts(self):
        username, password = 'user1', '12345'
        cursor, connection = self.connection_to_database
        try:
            cursor.execute("USE users")
            query = '''INSERT INTO `accounts` (`username`, `password`, `date_of_create`) VALUES (%s, %s, NOW())'''
            cursor.execute(query, (username, password))

        except Exception as error_type:
            return f"{error_type}"
        else:
            return "Succesfully created..."
        finally:
            connection.commit()
            cursor.close()
            connection.close()

    @property
    def create_character(self, health, mana, attack, balance, experience, level, job):
        return health, mana, attack, balance, experience, level, job
    def update_character(self):
        health, mana, attack, balance, experience, level, job = self.create_character
        cursor, connection = self.connection_to_database
        try:
            cursor.execute("USE users")
            cursor.execute("SELECT id FROM accounts ORDER BY id DESC LIMIT 1")
            acc_id = cursor.fetchone()['id']
            query = '''INSERT INTO `characters` (`health`, `mana`, `attack`, `balance`, `experience`, `level`, `job`, `account_id`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
            cursor.execute(query, (health, mana, attack, balance, experience, level, job, acc_id))
        except Exception as error_type:
            return f"{error_type}"
        finally:
            connection.commit()
            cursor.close()
            connection.close()

    def log_check(self, username, password):
        print(f"{username} {password}")
        cursor, connection = self.connection_to_database
        cursor.execute("USE users")
        cursor.execute("SELECT password FROM accounts WHERE username = %s", (username))
        result = cursor.fetchone()
        if result == password:
            print("password")
        else:
            print("what")



class Interface(Database):
    def __init__(self):
        pass

    def interraction_with_user(self):
        from difflib import get_close_matches
        greetings()
        user_input = input("Log In(1) or Create New Account(2)")


    def greetings(self):
        print("Wellcome To Basic Console RPG Game")
