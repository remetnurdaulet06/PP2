class Account:
    def __init__(self):
        self.owner = input("Your name: ")
        self.balance = 0
    def deposit(self, amount_of_money):
        self.balance += amount_of_money
        print()
        print(f"{amount_of_money} was added to your balance.")
        print(f"Your current balance: {self.balance}")
        print()
    def withdraw(self, amount_to_take):
        if amount_to_take <= self.balance:
            print("Successfully !, good luck :D", f"{amount_to_take} was taken from your balance.")
            self.balance -= amount_to_take
            print()
            print(f"Your current balance: {self.balance}")
            print()
        else:
            print()
            print("Oops!, your current balance is less than you want to take !")
            print()
            print(f"Your current balance: {self.balance}, but you want to take {amount_to_take}.")
asd = Account()
asd.deposit(5000)
asd.withdraw(2500)
asd.withdraw(5000)
print()