from atm_operation_module import cash_deposit, cash_withdraw, display_balance, mini_statement
from authentication_module import authenticate
accounts = {
    "rupay": 2000,
    "visa": 5000,
    "mastercard": 8499
}

transactions = []
if authenticate():
    while True:
        print("\nSelect an option:")
        print("1. Check Balance")
        print("2. Cash Withdraw")
        print("3. Cash Deposit")
        print("4. Mini Statement")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_balance(accounts)
        elif choice == 2:
            account_type = input("Enter account type (rupay/visa/mastercard): ")
            amount = float(input("Enter amount to withdraw: "))
            cash_withdraw(accounts, account_type, amount)
            transactions.append(f"Withdrawal from {account_type}: -{amount}")
        elif choice == 3:
            account_type = input("Enter account type (rupay/visa/mastercard): ")
            amount = float(input("Enter amount to deposit: "))
            cash_deposit(accounts, account_type, amount)
            transactions.append(f"Deposit to {account_type}: +{amount}")
        elif choice == 4:
            mini_statement(transactions)
        elif choice == 5:
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice. Please try again.")
