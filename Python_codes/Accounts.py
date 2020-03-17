import datetime


class Account:

    @staticmethod
    def _current_utctime():
        return datetime.datetime.utcnow()

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
        self.__transaction_list = [(Account._current_utctime(), 0)]
        print("new Account created for {}, current balance: {}".format(self.__name, self.__balance))

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transaction_list.append((Account._current_utctime(), amount))
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            self.__transaction_list.append((Account._current_utctime(), -1 * amount))
        else:
            print("amount not valid,")
        self.show_balance()

    def show_balance(self):
        print("Name: {} Balance is {}".format(self.__name, self.__balance))

    def show_transactions(self):
        print("---Transaction list----")
        for time, amount in self.__transaction_list:
            if amount < 0:
                tran_type = "withdraw"
                amount = -1 * amount
            else:
                tran_type = "deposit"
            print("balance: {} trans_type: {} time: {}".format(amount, tran_type, time))


if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.deposit(1000)
    tim.show_transactions()
    tim.withdraw(200)
    tim.show_transactions()

    tim.deposit(1000)
    tim.withdraw(20000)
