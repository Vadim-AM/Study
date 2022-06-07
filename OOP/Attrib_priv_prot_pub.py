class BankAccount:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def get_balance(self):
        print('get balance')
        return self.__balance

    def set_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def del_balance(self):
        print('delete balance')
        del self.__balance

    my_balance = property(get_balance)
    my_balance = my_balance.setter(set_balance)
    my_balance = my_balance.deleter(del_balance)


acc1 = BankAccount('Vadim', 1000)
print(acc1.my_balance)
acc2 = BankAccount('User', 2000)
print(acc2.my_balance)
acc2.set_balance(3000)
print(acc2.my_balance)