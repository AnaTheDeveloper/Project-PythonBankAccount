from BankModel.Bank import Bank
from BankModel.HSBC import Hsbc
from BankModel.Lloyds import Lloyds
from BankModel.Natwest import Natwest

if __name__ == '__main__':

    #Created a new Ana object

    AnasBankAccount = Bank("Ana", "Edwards")
    print("Start Result: ", AnasBankAccount.__repr__())

    AnasBankAccount.see_balance()

    AnasBankAccount.deposit(50)
    print("Your new balance is now: ", AnasBankAccount.__repr__())

    AnasBankAccount.withdraw(10)
    print("Your new balance is now: ", AnasBankAccount.__repr__())

    print("End Result: ", AnasBankAccount.__repr__())

    print("-------------------------------------------------------------------------------------")
    #Created a new Molly Object

    MollysBankAccount = Bank("Molly", "Jones")
    MollysBankAccount.deposit(100)
    MollysBankAccount.withdraw(25)
    MollysBankAccount.see_balance()

    #Created new HSBC/Natwest Banks

    lukesBankFromHSBC = Hsbc("Luke", "Brav")

    anasBankFromNatwest = Natwest("Ana", "Edwards")

    print(lukesBankFromHSBC.__repr__())
    print(anasBankFromNatwest.__repr__())

    lukesBankFromHSBC.sign_on_bonus()
    anasBankFromNatwest.sign_on_bonus()
    print(anasBankFromNatwest.__repr__())
    print(lukesBankFromHSBC.__repr__())

    person = Lloyds("person", "b")
    person.sign_on_bonus()

