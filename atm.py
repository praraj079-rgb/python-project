class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"\nCurrent Balance: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")

    def menu(self):
        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.check_balance()

            elif choice == "2":
                amount = float(input("Enter deposit amount: $"))
                self.deposit(amount)

            elif choice == "3":
                amount = float(input("Enter withdrawal amount: $"))
                self.withdraw(amount)

            elif choice == "4":
                print("Thank you for using the ATM!")
                break

            else:
                print("Invalid choice. Please try again.")


# Run the ATM
atm = ATM(100000000000)  # Starting balance
atm.menu()