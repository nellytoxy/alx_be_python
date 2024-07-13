class BankAccount:
    def __init__(self,name):
        self.name=name
        self.balance = 0

    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance + self.amount
        print(f"{self.balance}, $")
    def withdraw(self,amount):
        self.amount=amount
        if self.balance < self.amount:
            print(f"insufficient funds please top up")
        else:
            self.balance=self.balance - self.amount
            print(f"{self.balance}, $")
    def display_balance(self):
        display_balance=self.balance
        print(f"{display_balance}, Current Balance:")
        