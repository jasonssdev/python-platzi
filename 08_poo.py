class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old")

person_1 = Person(name="Jason", age="34")
person_2 = Person(name="Laura", age="32")

person_1.greet()
person_2.greet()

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"A deposit for {amount} has been done, the current balance is {self.balance}")
        else:
            print("deposit invalid, inactive account")

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} has been withdrawn, the current balance is {self.balance}")

    def deactivate_account(self):
        self.is_active = False
        print("Bank Account has been deactivated")

    def activate_account(self):
        self.is_active = True
        print("Bank Account has been activated")

account_1 = BankAccount(account_holder="Jason", balance=5000)
account_2 = BankAccount(account_holder="Laura", balance=10000)

account_1.deposit(2000)
account_2.deposit(1000)
account_1.withdraw(500)
account_2.withdraw(700)
account_1.deactivate_account()
account_1.deposit(100)
account_2.deposit(300)
account_1.activate_account()
account_1.deposit(99)








