from account import Account

class ChildrenAccount(Account):
    def deposit(self, amount):
        self.balance += amount * 0.007
        super().deposit(amount)


    def withdraw(self, amount):
        print("No withdrawals are allowed for children account")

d = ChildrenAccount()
d.deposit(1000)
d.withdraw(10)
