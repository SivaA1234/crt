#create a atm system subtasks
#display the remaining amount in the atm
#three accounts rupay2000, visa 5000,mastercard8499
#authentication of user if the user is authenticated then give him the following auctions choose first check balance ,cash withdraw,cash deposit
#mini statement of the last three transactions
# authentication_module.py

def authenticate():
    username = input("Enter username: ")
    password = input("Enter password: ")
    valid_username = "harshith"
    valid_password = "harshith"

    if username == valid_username and password == valid_password:
        return True
    else:
        print("Invalid username or password")
        return False
