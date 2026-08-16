class BankAccount:
    def __init__(self,name,account_number,balance):
        self.name=name
        self.account_number=account_number
        self.balance=balance
    def display(self):
        print("name: ",self.name)
        print("account_number: ",self.account_number)
        print("balance: ",self.balance)
    def deposite(self,amount):
        self.balance= self.balance+amount
        print("balance:",self.balance)
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance= self.balance-amount
            print("withdraw:",amount)
        else:
            print("INSUFFICIENT BALANCE")
    def add_interest(self,rate):
        interest =self.balance*rate/100
        self.balance=self.balance+interest
        print("interest:", interest)
        print("New balance:",self.balance)
        print("INTREST ADDED")
        
b1=BankAccount("gokul",456789890,0)
b1.display()

b1.deposite(110000)
b1.display()

b1.withdraw(300)
b1.display()

b1.add_interest(100)
        
