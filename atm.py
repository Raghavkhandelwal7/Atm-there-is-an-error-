class Atm():
    def __init__(self,atmCardNumber,pinNumber):
        self.atmCardNumber=atmCardNumber
        self.pinNumber=pinNumber

    def atmCardNumber(self):
        return self.atmCardNumber

    def pinNumber(self):
        return self.pinNumber

    balance=100000

    print("Welcome to you atm!")
    print("How can we help?")
    print("the first input would be for withdrawl and the second would be for depositon also the third input would be for checking you balance")

    withdrawl=int(input("Withdraw you cash: "))
    balance=balance-withdrawl

    if balance<withdrawl:
        print("insufficent funds try again or try adding more money into your account")

    deposition=int(input("Add money to your account(enter 0 if you dont want to): "))
    balance=balance+deposition

    print("Your balance is: ", balance)

account1 = Atm('1034956781234','6734')
print(account1.atmCardNumber())
print(account1.pinNumber())
