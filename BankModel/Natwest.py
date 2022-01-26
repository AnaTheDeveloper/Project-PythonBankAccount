from BankModel.Bank import Bank

class Natwest(Bank):

    def __init__(self, forename, surname):
        super().__init__(forename,surname)

    def sign_on_bonus(self):
        self.balance = self.balance + 2000
