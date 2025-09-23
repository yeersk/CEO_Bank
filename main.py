import bank_api
new_contragent = bank_api.account()

if __name__ == "__main__":
    while True:
        text = input('function')
        if hasattr(new_contragent, text):
            func = getattr(new_contragent, text)
            print(func())
        else: print('function is not find')