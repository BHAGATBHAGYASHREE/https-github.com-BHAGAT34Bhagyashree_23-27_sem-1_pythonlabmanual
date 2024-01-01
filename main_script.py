# main_script.py
from bank_module import BankAccount

def main():
    account_holder_name = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance: "))

    account = BankAccount(account_holder_name, initial_balance)

    while True:
        print("\nBank Operations:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            print(f"Current Balance: ${account.check_balance()}")
        elif choice == '2':
            deposit_amount = float(input("Enter the deposit amount: "))
            account.deposit(deposit_amount)
        elif choice == '3':
            withdrawal_amount = float(input("Enter the withdrawal amount: "))
            account.withdraw(withdrawal_amount)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
