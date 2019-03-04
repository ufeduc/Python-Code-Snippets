class Database:
    def __init__(self):
        self.data = []

    @property
    def connection_to_database(self):
        import pymysql.cursors
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='password',
                                     cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        return cursor, connection

    def create_database(self):
        cursor, connection = self.connection_to_database
        try:
            for line in open('create_database.sql'):
                cursor.execute(line)

        except Exception as error_type:
            return f"{error_type}"
        finally:
            connection.commit()
            cursor.close()
            connection.close()

    def create_accounts(self, username, password):
        cursor, connection = self.connection_to_database
        cursor.execute("USE users")
        try:
            query = '''INSERT INTO `accounts` (`username`, `password`, `date_of_create`) VALUES (%s, %s, NOW())'''
            cursor.execute(query, (username, password))

        except Exception as error_type:
            return f"{error_type}"
        else:
            print("Succesfully created...")
        finally:
            connection.commit()
            cursor.close()
            connection.close()


    def create_character(self, health, mana, attack, balance, experience, level, job):
        cursor, connection = self.connection_to_database
        cursor.execute("USE users")
        try:
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
        cursor, connection = self.connection_to_database
        cursor.execute("USE users")
        try:
            cursor.execute("SELECT * FROM accounts WHERE username = %s AND password = %s", (username, password))
            result = cursor.fetchone()
            connection.commit()
            cursor.close()
            connection.close()
            if result:
                return True
            else:
                return False
        except Exception as e:
            return f"Exception is: {e}"


    def user_check(self, username):
        cursor, connection = self.connection_to_database
        cursor.execute("USE users")
        try:
            cursor.execute("SELECT username FROM accounts WHERE username = %s", (username))
            result = cursor.fetchone()
            connection.commit()
            cursor.close()
            connection.close()
            if result:
                return True
            else:
                return False
        except Exception as e:
            return f"Exception is: {e}"

    def display_character(self, username, password):
        cursor, connection = self.connection_to_database
        cursor.execute("USE users")
        try:
            cursor.execute('''SELECT username, health, mana, attack, balance, experience, level, job FROM accounts INNER JOIN characters ON accounts.id = characters.account_id WHERE username = %s''', (username))
            self.data = cursor.fetchone()

        except Exception as e:
            return f"Error Has Occured: {e}"
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            return self.data


class Interface(Database):

    def __init__(self):
        self.log = ['log' ,'log in', '1']
        self.new = ['create', 'new', 'create new account', 'sign', 'sign up', '2']

    def greetings(self):
        print("Wellcome To Basic Console RPG Game")

    def interraction_with_user(self):
        from difflib import get_close_matches
        cursor, connection = Interface().connection_to_database
        cursor.execute("show databases")
        db_list = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        database_list = [db['Database'] for db in db_list if db['Database'] == 'users']
        if 'users' in database_list:
            Interface().greetings()
            user_input = input("Log In(1) or Create New Account(2): ")
            username = input('username: ')
            password = input('password: ')
            if get_close_matches(user_input.lower(), self.log):
                # print("1 log in")
                if Interface().log_check(username, password):
                    Interface().log_in(username, password)
                else:
                    print("Password Did Not Matched...")
            elif get_close_matches(user_input.lower(), self.new):
                # print("2 create new account")
                if Interface().user_check(username):
                    print("Username Already Used...")
                else:
                    print("Create Initializing...")
                    Interface().create_account(username, password)
            else:
                print("wrong input")
        else:
            print("Installing Database...")
            Interface().create_database()
            print("Succesfully Installed...")


    def log_in(self, username, password):
        character_info = Interface().display_character(username, password)
        print("===============")
        for k,v in character_info.items():
            print(f"{k}: {v}")
        print("===============")
        # print(character_info)



    def create_account(self, username, password):
        from character import Character
        Interface().create_accounts(username, password)
        job = input("Warrior(1) Assassin(2) Mage(3): ")
        properties = Character(job).interraction_with_character_class()
        Interface().create_character(properties[0], properties[1], properties[2], properties[3], properties[4], properties[5], properties[6])
        c = Interface().display_character(username, password)
        print("===============")
        for k,v in c.items():
            print(f"{k}: {v}")
        print("===============")


# Database().log_check('user1','12345')
Interface().interraction_with_user()
# print(Database().create_accounts('user123','123123'))
