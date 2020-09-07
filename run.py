import random
from user import User
from credentials import Credetials

def main():

    while True:
        print("Welcome to pasword locker")
        print("\n")
        print("Select a short code to navigate through:to login 'lg',to exit 'ex':to create a new user 'nu'")
        short_code = input().lower() 
        print("\n")

    if short_code == 'nu':
        print("Create username")
        created_user_name = input(any)

        print("Create password")
        created_user_password = input(any)

        print("Confirm password")
        confirm_password = input()
    
    while confirm_password != created_user_password:
        print("Invalid password")
        print("Input password")
        created_user_password = input()
        print("Confirm your password")
        confirm_password = input()

    else:
        print("Correct {created_user_password}! Account created successfully")
        print('\n')
        print("Login")
        print("Username")
        enter_username = input()
        print("Enter your password")
        confirm_password = input(any)

    while entered_username != created_user_name or entered_password != created_user_password:
        print("Invalid password  or username")
        print("Username")
        entered_username = input()
        print("Your password")
        entered_password = input()

    else:
        print("Welcome! (entered_username) to your password")
        print("\n")

    else short_code == 'lg'
        print("Welcome")
        print("Enter your name")
        default_user_name = input()

        print("Enter your password")
        default_user_password = input()
        print('\n')
        while default_user_name != 'testuser' and password '08851550':
            print("Wrong username or password", username 'testuser' and password '08851550')
            print("Enter username")
            default_user_name = input()
            print('\n')

        else:
            print("Login username")
            print('\n')
            print('\n')

        else short_code == 'ex'
            break
        else:
            print("Enter valid code to continue")
        
        if __name__ == '__main__':
            main()

