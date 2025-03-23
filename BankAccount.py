class SavingAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: ${amount}. New balance: ${self.balance}"
    def withdrawl(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        self.balance -= amount
        return f"Withdrawl: ${amount}. New balance: ${self.balance}"
    def transfer(self, amount, recipient):
        if amount > self.balance:
             print("Insufficient funds")
        self.balance -= amount
        recipient.deposit(amount)
        return f"Transferd: ${amount}. Your new balance: ${self.balance}"
    def getBlance(self):
        return f"Current balance: ${self.balance}"
    
class CheckingAccount:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: ${amount}. New balance: ${self.balance}"
    
    def withdrawl(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        self.balance -= amount
        return f"Withdrawl: ${amount}. New balance: ${self.balance}"
    
    def transfer(self, amount, recipient):
        if amount > self.balance:
            print("Insufficient funds")
        self.balance -= amount
        recipient.deposit(amount)
        return f"Transferred: ${amount}. Your new balance: ${self.balance}"
    def getBlance(self):
        return f"Current balance: ${self.balance}"
    
def main():
    print("Wellcome to the banking system.")
    
    savings_balance = float(input("Enter initial amount for the saving account: "))
    checking_balance = float(input("Enter initial amount for the cheking account: "))
    
    saving = SavingAccount(savings_balance)
    checking = CheckingAccount(checking_balance)
    
    while True:
        print("\nChoose Account Type:")
        print("1. Savaing Account")
        print("2. Checking Account")
        print("3. Exit")
        
        account_choice = input("Enter your choice (1-3): ")
        
        if account_choice == "1":
            current_acount = saving
            account_type = "Saving"
        elif account_choice == "2":
            current_acount = checking
            account_type = "Checking"
        elif account_choice == "3":
            print("Thank you for using our Bank System! Goodbye.")
            break
        else:
             print("Invalid choice. Please try again.")
             continue
         
        while True:
            print(f"\n{account_type} Account - Choose an action:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Check Balance")
            print("5. Switch Account / Exit")
            
            action_choice = input("Enter your choice (1-5): ")
            
            if action_choice == "1":
                amount = float(input("Enter deposit amount: "))
                print(current_acount.deposit(amount))
                
            elif action_choice == "2":
                amount = float(input("Ente withdrawal amount: "))
                print(current_acount.withdrawl(amount))
                
            elif action_choice == "3":
                amount = float(input("Enter transfer amount: "))
                recipient = saving if current_acount == checking else checking
                print(current_acount.transfer(amount, recipient))
                
            elif action_choice == "4":
                print(current_acount.getBlance())
            
            elif action_choice == "5":
                break
            
            else:
                print("Invalid choice. Please try again.")
main()
            
            
    
    
