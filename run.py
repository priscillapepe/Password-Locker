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
        

    if __name__ == '__main__':
    main()

