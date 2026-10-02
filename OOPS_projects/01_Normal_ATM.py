class Atm:
    def __init__(self):
        self.balance = 0
        self.pin = ""

    def menu(self):
        user_input = int(input("""
        Hello, Welcome to ATM service:
        1. Enter: 1 to set pin
        2. Enter: 2 to deposite 
        3. Enter: 3 to withdraw
        4. Enter: 4 to check balance
        5. Enter: 5 to exit
        Enter your choice: """))
        
        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.deposite()
        elif user_input == 3:
            self.withdraw()
        elif user_input == 4:
            self.check_balance()
        else:
            print("Bye")

    def create_pin(self):
        self.pin = input("Enter the pin to set: ")
        print("Your pin is set")
        self.menu()

    def deposite(self):
        pin = input("Enter your ATM pin: ")
        if pin == self.pin:
            amount = int(input("Enter the amount that you want to deposite: "))
            self.balance += amount
            print(f"{amount} amount deposited")
        else:
            print("Invalid pin")
        self.menu()

    def withdraw(self):
        pin = input("Enter your ATM pin: ")
        if pin == self.pin:
            amount = int(input("Enter the amount that you want to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} amount withdrawn from your account")
            else:
                print("Insufficient funds")
        else:
            print("Invalid pin")
        self.menu()

    def check_balance(self):
        pin = input("Enter your ATM pin: ")
        if pin == self.pin:
            print(f"Your current balance is: {self.balance}")
        else:
            print("Invalid pin")
        self.menu()
