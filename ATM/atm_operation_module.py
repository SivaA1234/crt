def display_balance(accounts):
    print("Remaining balance:")
    for account, balance in accounts.items():
        print(f"{account}: {balance}")

def cash_withdraw(accounts, account_type, amount):
    if account_type in accounts:
        if accounts[account_type] >= amount:
            accounts[account_type] -= amount
            print(f"Withdrawal successful. Remaining balance: {accounts[account_type]}")
        else:
            print("Insufficient balance")
    else:
        print("Invalid account type")

def cash_deposit(accounts, account_type, amount):
    if account_type in accounts:
        accounts[account_type] += amount
        print(f"Deposit successful. New balance: {accounts[account_type]}")
    else:
        print("Invalid account type")

def mini_statement(transactions):
    print("Mini Statement - Last three transactions:")
    for transaction in transactions[-3:]:
        print(transaction)
