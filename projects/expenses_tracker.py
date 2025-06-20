#Display command options to the user in the CLI

def user_CLI_menu():
    print("\nHello! Welcome to Expense Tracker \n \nSelect an option to continue ")
    print("[1] Add new transaction \n[2] View all transactions \n[3] View balance \n[4] Summary by category \n[5] Press q to Exit")

user_CLI_menu()

#This class defines the transcation, it is further inheritated by other classes

class Transactions:
    #constructor
    def __init__(self, amount, type, category, description):
        self.amount = amount
        self.type = type
        self.category =category
        self.discription = description
        
    #method
    
class Add_transaction(Transactions):
    def __init__(self, amount, type, category, description):
        super().__init__(amount, type, category, description)
        
    def prompt_user_to_add_transaction(self):
         pass
        
        