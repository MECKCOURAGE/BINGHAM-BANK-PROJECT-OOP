class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Account balance is: ", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("Account balance is: ", self.balance)




#d = Account()
#d.deposit(1000)
