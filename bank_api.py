import time
import sqlite3

class account:
    def __init__(self):
        self.__db__ = sqlite3.connect('BANK.db') 
        self.__cursor__ = self.__db__.cursor()
        self.__user_id = None
        self.__name = ''
        self.__surname = ''
        self.__login = ''
        self.__password = ''


    def quit(self):
        print('london, goodbye')
        time.sleep(2.5)
        print(f'yi{'e'*10*6}')
        quit()

    def check_sql(self, value):
        banned = ['=', '<', '>', '<=', '>=', '<>']
        for ch in value: #checking for sql-injection | проверка против sql-инъекции
                if ch in banned:
                    print('you are banned by sql')
                    return False
        return True 

    def check_info(self):
        if self.__user_id is not None:
            return f"name: {self.__name} \nsurname: {self.__surname}"
        else: return "you're not authorised"

    def authorisation(self):
        login, password_by_user = input('login \n'), input("password \n")

        try:
            self.check_sql(password_by_user)
            
            self.__cursor__.execute("""SELECT * FROM users WHERE login = (?) AND password = (?)""", (login, password_by_user))
            user_info = self.__cursor__.fetchone()
            
            if user_info is not None:
                user_info = list(user_info)
                self.__user_id = user_info[0]
                self.__name = user_info[1]
                self.__surname = user_info[2]
                self.__login = user_info[3]
                self.__password = user_info[4]
                
            else:
                return 'login or password are incorrect'

            return f'welcome, {self.__login}'
        except: return 'sorry, bag'

    def logout(self):
        if self.__user_id is not None:
            self.__user_id = None
            self.__name = ''
            self.__surname = ''
            self.__login = ''
            self.__password = ''
            return "you've successfully logged out"
        else: return "you're no authorised"

    def create(self):
        self.__cursor__.execute('''SELECT login FROM users''') # select all LOGIN from table USERS | собираем все ЛОГИНЫ из таблицы USERS
        logins = self.__cursor__.fetchall() # variable will keep all logins |  переменная будет хранить все логины

        name, surname, login, password = input('name\n'), input('surname\n'), input('login\n'), input("password \nset value with lenght >= 8 \nplese, dont use '=', '<', '>', '<=', '>=', '<>' \n") 
        if len(password) < 8: return 'please, set value with lenght >= 8'
        
        while True:
            for ch in logins: # going in logins
                ch = list(ch)
                if login in ch:
                    return 'account with login "{login}" already exists'

            self.__cursor__.execute('''INSERT INTO users (name, surname, login, password) VALUES (?, ?, ?, ?)''', (name, surname, login, password))

            self.__db__.commit()
            
            return 'account has created'
    
    def delete(self):
        if input('Are you sure? (y/n?) ').lower() == 'y':
            password_by_user = input("input youre password ")
            if password_by_user == self.__password:
                self.__cursor__.execute("""DELETE FROM users WHERE user_id = (?)""", (self.__user_id,))
                self.__db__.commit()
                return 'account is have just deleted'
            else: return 'incorrect password, goodbye'
        else: return 'nu, ladno'

    def password_change(self):
        if self.__user_id is not None:
            self.__cursor__.execute('''SELECT password FROM users WHERE user_id = (?)''', (self.__user_id,))

            password_from_db = list(self.__cursor__.fetchone())[0]
            password_from_user = input('please, input your old password ')

            if password_from_db == password_from_user:
                new_password_from_user = input("please, set new password \nset value with lenght >= 8 \nplese, dont use '=', '<', '>', '<=', '>=', '<>' \n")
                if self.check_sql(new_password_from_user) and len(new_password_from_user) >= 8:

                    self.__cursor__.execute('''UPDATE users SET password = (?) WHERE user_id = (?)''', (new_password_from_user, self.__user_id))
                    self.__db__.commit()

                    return 'new password have successfully change'
                
                else: "plese, dont use '=', '<', '>', '<=', '>=', '<>' and set value with lenght >= 8"
            else: return 'password is incorrect'
        
        else: return 'please, authorise'
    
    
    
