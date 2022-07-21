class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance
        
    def deposit(self, amount):

        self.balance=self.balance+amount
        print(f"Balance:{self.balance}")
        return self
        
    def withdraw(self, amount):

        if amount>self.balance:
            print(f"Insuffuicient Funds: {self.balance}")
        else:
            self.balance=self.balance-amount
            print(f"New Balance: {self.balance}")
        return self
            
    def display_account_info(self):
        print(f"Account Balance: {self.balance}")
        return self
    # def yield_interest(self):
    #     self.interest_yeild=interest_yeild

checkings=BankAccount(0.2, 0)
checkings.deposit(100).deposit(20).deposit(350).withdraw(25).display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.amount=amount

    def example_method(self):
        self.account.deposit(100)		# we can call the BankAccount instance's methods
    # print(self.account.balance)		# or access its attributes

