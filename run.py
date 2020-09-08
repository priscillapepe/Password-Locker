import random
from user import User

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
        
            if confirm_password != created_user_password:
                print("Invalid password")
                print("Input password")
                created_user_password = input()
                print("Confirm your password")
                confirm_password = input()

            else :
                print("Correct(created_user_password)!Account created successfully")
                print('\n')
                print("Login")
                print("Username")
                enter_username = input()
                print("Enter your password")
                confirm_password = input(any)

            while enter_username != created_user_name or confirm_password != created_user_password:
                print("Invalid password  or username")
                print("Username")
                enter_username = input()
                print("Your password")
                enter_password = input()

            else:
                print(f"Welcome! {enter_username} to your password")
                print("\n")

        elif short_code == 'lg':
            print("Welcome")
            print("Enter your name")
            default_user_name = input()

            print("Enter your password")
            default_user_password = input()
            print('\n')

            while  default_user_name != 'testuser' and default_user_password !='08851550':
                print("Wrong username or password, username 'testuser' and password '08851550'")
                print("Enter username")
                default_user_name = input()
                print('\n')

            else:
                print("Login username")
                print('\n')
                print('\n')

        elif short_code == 'ex':
            print('goodbye-----')
            break
        else:
            print("Enter valid code to continue")
        
if __name__ == '__main__':
             main()

