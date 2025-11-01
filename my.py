class bankaccount :
    def __init__(self,owner,balance = 0) :
        self.owner = owner
        self.balance = balance

    def deposit(self,amount) :
            self.balance += amount
            print(f"succecsfully deposited. the total balance is RS : {self.balance}")

    def withdraw(self,amount) :
        if amount > self.balance :
            print("sorry!.you are broke brother")
        else :    
            self.balance -= amount
            print(f"succecsfully withdrawed. the total balance is RS : {self.balance}")

    def showbalance(self) :
        print(f"the current balance is : {self.balance}")

s = bankaccount("hirusha",50000)
s.deposit(1000)
s.withdraw(51001)
s.showbalance()

