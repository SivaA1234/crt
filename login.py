#write a login func which accepts a user only when user name and password or same and displays a message login successfull
#otherwise it keeps asking the user until they are correct
def login():
    while True:
        x=input("enter the username:")
        y=input("enter the password:")
        if x==y:
            print("succesfull login")
            break
        else:
            print("login unsucessfull")
            print("enter the credential correct")
login()
        
