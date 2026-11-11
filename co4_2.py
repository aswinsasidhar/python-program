class BankAccount:

    def __init__(self, account_number, name, account_type, balance):

        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount
        print("Amount deposited:", amount)
        print("Current balance:", self.balance)

    def withdraw(self, amount):

        if amount <= self.balance:

            self.balance -= amount

            print("Amount withdrawn:", amount)

            print("Current balance:", self.balance)

        else:

            print("Insufficient balance")

    def display(self):

        print("\nAccount Details")

        print("Account Number:", self.account_number)

        print("Name:", self.name)

        print("Account Type:", self.account_type)

        print("Balance:", self.balance)

# Creating bank account

acc = BankAccount(8533540, "ASWIN SASIDHAR", "Savings", 50000)

acc.display()
acc.deposit(2000)
acc.withdraw(1000)
