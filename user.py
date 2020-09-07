from credentials import Credetials

class User:
    def __init__(self):
        self.username = None
        self.password = None
        self.credentials = Credetials()
        self.isLoggedIn = False
    def create_new_user(self,username,password):
        self.username = username
        self.password = password
        print("Account created successfully.")
        self.isLoggedIn = True
    def view_accounts(self):
        for ac in self.credentials.accounts:
            print(ac)
        return self.credentials.accounts
    def sign_in(self,username,password):
        if username == self.username and password == self.password:
            self.isLoggedIn = True
        else:
            return "Incorrect Username/ Password."
    def log_out(self):
        self.isLoggedIn= False