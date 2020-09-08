from string import ascii_letters,digits,punctuation
from secrets import choice
class Credetials:
    def __init__(self):
        self.accounts = []
    def new_account(self,account_name,username,password=None):
        if password is None:
            user_input = int(
                input('Specifify the length of password needed: ')
            )
            password = self.generate_password(user_input)
        account = {'account_name':account_name,'username':username,'password':password}
        self.accounts.append(account)
        print("Account created sucessfully.")
        return account
    
    def generate_password(self,length=8):
        alphabet = ascii_letters + digits + punctuation
        return ''.join(choice(alphabet) for i in range(length))
    def get_account_details(self,account_name):
        for ac in self.accounts:
            if ac['account_name'] == account_name:
                return ac
    
    def delete_account(self,account_name):
        """
        Accepts account name as argument. 
        Deletes it from accounts credentials       

        """
        # new_accs =[]
        # for ac in self.accounts:
        #     if not(ac.get('account_name')==account_name):
        #         new_accs.append(ac)        
        # self.accounts = new_accs
        self.accounts = [ac for ac in self.accounts if not(ac.get('account_name')==account_name)]       
        print ("Account deleted successfully.")
    

# c = Credetials()
# print(c.generate_password(30))
# print(c.new_account('ig','ig_acc','p@$$w0rd'))
# print(c.new_account('fb','facebook','@n0ther|p@$$w0rd'))
# print("====================================================")
# print(c.get_account_details('ig'))
# print(c.delete_account('erty'))
# print(c.accounts)



