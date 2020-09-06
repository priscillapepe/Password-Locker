from makesure import User

def new_student(fname, lname, passwrd):
    new_user = User(fname, lname, passwrd)
    return new_user

def create_user(user):
    User.save_user(user)

def main():
    print("Hello what is your first name?")
    fname = input()
    print("Whats your last name?")
    lname = input()
    print("What's your user password")
    passwrd = input()
    created_user = new_student(fname, lname, passwrd)
    create_user(created_user)

    print("New user", fname, "Created")

if __name__ == "__main__":
    main()








