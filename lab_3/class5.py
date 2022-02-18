class bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, money):
        self.money = money
        self.balance = self.balance + self.money
        print('You have',self.balance)
    def withdraw(self, money):
        self.money = money
        if self.money <= self.balance:
            self.balance = self.balance - self.money
            print(self.balance, "left" )

        else:
            print(self.owner, " you cannot fool us")
stat = bank('Almat', 500000)
stat.withdraw(500)
stat.deposit(500)