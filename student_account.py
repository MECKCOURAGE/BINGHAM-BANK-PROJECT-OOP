from account import Account


class StudentAccount(Account):
    def deposit(self, amount):
        if amount <= 50000:
            super().deposit(amount)
        else:
            print("You have reached your deposit limit")

    def withdraw(self, amount):
        if amount <= 2000:
            super().withdraw(amount)
        else:
            print("You have reached your withdrawal limit")

d = StudentAccount()
d.withdraw(20000)
