class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance=self.balance+amount
            print(f"Deposited {amount} successfully. New balance is {self.balance}.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance=self.balance-amount
                print(f"Withdrew {amount} successfully. New balance is {self.balance}.")
            else:
                print("Insufficient balance")
        else:
            print("Withdrawal amount must be greater than 0.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")


# Create a bank account for an individual
acc=BankAccount("RAJ", 5000)  # Starting with a balance of 5000

# Show account info
acc.display_account_info()

# Deposit money
acc.deposit(400)

# Withdraw money
acc.withdraw(150)

# Check balance
acc.check_balance()

# Another user with default balance (0)
acc1 = BankAccount("Shyam",2000)

# Show Bob's account info
acc1.display_account_info()
acc1.deposit(10000)
acc1.withdraw(2000)
acc1.check_balance()
