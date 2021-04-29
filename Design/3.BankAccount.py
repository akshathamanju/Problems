class BankAccount(object):
    def __init__(self):
        self.balance = 0

    def witdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def display_balance(self):
        print("\n Available balance : ", self.balance)
obj1 = BankAccount()
obj2 = BankAccount()
print("obj1.deposit(100)", obj1.deposit(100))
obj1.display_balance()
print("obj2.deposit(50)", obj2.deposit(50))
obj2.display_balance()
print("obj1.witdraw(10)", obj1.witdraw(10))
obj1.display_balance()
'''
Inheritance
Let us try to create a little more sophisticated account type 
where the account holder has to maintain a pre-determined minimum balance.
'''

class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print("cannot withdraw, need to maintain minimum balance")
        else:
            BankAccount.witdraw(self, amount)
obj3 = MinimumBalanceAccount(100)
obj4 = MinimumBalanceAccount(100)
print("obj3.deposit(100)", obj3.deposit(100))
print("obj4.deposit(50)", obj4.deposit(50))
print("obj3.witdraw(10)", obj3.withdraw(10))

