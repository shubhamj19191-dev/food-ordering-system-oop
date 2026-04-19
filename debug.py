class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} jama ho gaye! Balance: {self.balance}")

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} nikaal liye! Balance: {self.balance}")
        else:
            print("Bhai itne paise nahi hain!")

    def show_balance(self):
        print(f"{self.owner} ka balance: {self.balance}")


acc1 = BankAccount("Raj", 1000)
acc1.deposit(500)
acc1.withdraw(200)
acc2 = BankAccount("Amit",1000)
acc2.show_balance()