from abc import ABC, abstractmethod

class Bank(ABC):

    def __init__(self, forename, surname):
        self.forename = forename
        self.surname = surname
        self.balance = 0


    def __repr__(self):
        return str(self.__dict__)

    def deposit(self, money_to_deposit):
        self.balance = self.balance + money_to_deposit
        print("You deposited: ", money_to_deposit)


    def withdraw(self, money_to_withdraw):
        self.balance = self.balance - money_to_withdraw
        print("You withdrew: ", money_to_withdraw)


    def see_balance(self):
        print("Your current balance is: ", self.balance)

    # Optional Method for child classes of the Bank super to use
    def sign_on_bonus(self):
        print("There is no sign on bonus!")
        pass