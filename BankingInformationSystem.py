import json
import os

class Account:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = [f"Account created with balance: ₹{balance}"]

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ₹{amount}")
            print(f"✅ Successfully deposited ₹{amount}")
        else:
            print("❌ Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient balance!")
        elif amount > 0:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: ₹{amount}")
            print(f"✅ Successfully withdrawn ₹{amount}")
        else:
            print("❌ Invalid withdrawal amount!")

    def display_balance(self):
        print(f"\n🔹 Account Holder: {self.account_holder}")
        print(f"💰 Balance: ₹{self.balance}")

    def show_transaction_history(self):
        print(f"\n📜 Transaction History for {self.account_holder}:")
        for transaction in self.transaction_history:
            print(transaction)

class BankingSystem:
    def __init__(self, filename="accounts.json"):
        self.filename = filename
        self.accounts = self.load_accounts()

    def load_accounts(self):
        """ Load accounts from a JSON file """
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
            return {name: Account(name, acc["balance"]) for name, acc in data.items()}
        return {}

    def save_accounts(self):
        """ Save accounts to a JSON file """
        data = {name: {"balance": acc.balance, "transactions": acc.transaction_history} for name, acc in self.accounts.items()}
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def create_account(self):
        name = input("Enter Account Holder Name: ").strip().lower()
        if name in self.accounts:
            print("❌ Account already exists!")
            return
        try:
            balance = float(input("Enter Initial Deposit Amount: "))
            self.accounts[name] = Account(name, balance)
            self.save_accounts()
            print(f"✅ Account created successfully for {name.capitalize()}")
        except ValueError:
            print("❌ Invalid amount! Please enter a valid number.")

    def find_account(self):
        name = input("Enter Account Holder Name: ").strip().lower()
        if name in self.accounts:
            return self.accounts[name]
        print("❌ Account not found!")
        return None

    def deposit_money(self):
        account = self.find_account()
        if account:
            try:
                amount = float(input("Enter Deposit Amount: "))
                account.deposit(amount)
                self.save_accounts()
            except ValueError:
                print("❌ Invalid amount! Please enter a valid number.")

    def withdraw_money(self):
        account = self.find_account()
        if account:
            try:
                amount = float(input("Enter Withdrawal Amount: "))
                account.withdraw(amount)
                self.save_accounts()
            except ValueError:
                print("❌ Invalid amount! Please enter a valid number.")

    def check_balance(self):
        account = self.find_account()
        if account:
            account.display_balance()

    def show_transaction_history(self):
        account = self.find_account()
        if account:
            account.show_transaction_history()

    def start(self):
        while True:
            print("\n1️⃣ Create Account")
            print("2️⃣ Deposit Money")
            print("3️⃣ Withdraw Money")
            print("4️⃣ Check Balance")
            print("5️⃣ Show Transaction History")
            print("6️⃣ Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.deposit_money()
            elif choice == "3":
                self.withdraw_money()
            elif choice == "4":
                self.check_balance()
            elif choice == "5":
                self.show_transaction_history()
            elif choice == "6":
                print("✅ Thank you for using the Banking Information System. Goodbye!")
                break
            else:
                print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    system = BankingSystem()
    system.start()
