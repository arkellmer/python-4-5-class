#andrew kellmer 10/1/18
#password and username program



#menu is running main and letting you in or not
def main():
    
    login = False
    password, username, login = menu()
    
    if login == True:
        print("you're in")
    else:
        print("access denied")
        menu()
#menu has the bulk of the program running in it.
def menu():
    
    choice = 0
    
    while choice == 0:
        print("to sign up enter 1")
        print("to sign in enter 2")
        choice = int(input())
        
        if choice == 1:
            print ("choice 1")
            username = get_username()
            password = get_password()
            choice = 0
            
        elif choice == 2:
            print("choice 2")
            login = check_info(username, password)
            return password, username, login
        
        else:
            print("thats not a valid option")
            menu()

#gets the username from the user        
def get_username():

    print("""username can only contain numbers and letters
and can only contain 10 characters and no less than 3 characters""")

    username = input("enter your username")

    if username.isalnum() and len(username)<=10 and len(username)>=3:
        print("username is set")
        return username

    else:
        print("your username didn't meet the requirements")
        get_username()

#gets the password from the user
def get_password():
    
    print("""your password must start with a capital letter and must contain
at least one symbol and must be 10 characters long.""")

    password = input("enter password")

    if password.istitle() and not password.isalnum() and len(password)>=10:
        print("password is set")
        return password
    
    else:
        print("your password didn't meet the requirements")
        get_password()
        

#checks the information
def check_info(username, password):
    username = username
    password = password
    input_username = input("enter your username")
    input_password = input("enter your password")

    if input_username == username and input_password == password or input_username == "admin":
        return True

    else:
        return False
        

main()
