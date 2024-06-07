from account import Account

class SavingsAccount(Account):
    def deposit(self, amount):
            self.balance += amount * 0.005
            super().deposit(amount)

    def withdraw(self, amount):
        if amount <= 700000:
            super().withdraw(amount)
        else:
            print("You have reached your withdrawal limit")

d = SavingsAccount()
d.deposit(100000000)
