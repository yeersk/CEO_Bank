import time
class account:
    def __init__(self):
        self.__password = ''
        self.__balance = 0
        self.__admin = False  

    def quit(self):
        print('london, goodbye')
        time.sleep(2.5)
        print(f'yi{'e'*10*6}')
        quit()

    def password_set(self):
        value = input('set value')
        if len(value) >=8: 
            self.__password = value
            if self.__password == '123456789': 
                self.__admin = True 
                return 'welcome to admin_state'
            else: 
                self.__admin = False
                return 'accepted'
        else: return 'incorrect password'
    
    def password_check(self):
        value = input('set value')
        try: return value == self.__password
        except: return 'you are down'
    
    def balance_check(self):
        return self.__balance
    
    def balance_set(self):
        while True:
            if self.__admin:
                value = input(('set value'))
                if value.isdigit(): 
                    self.__balance += int(value)
                    return 'accepted'
                elif value == 'break': return 'break'
                else: 
                    print('please, set digital value')
            else: return 'kyky'