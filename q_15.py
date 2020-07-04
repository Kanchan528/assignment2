# Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?

class Banking:
    def __init__(self, acc_name, acc_num, acc_type, balance):
        self.acc_name=acc_name
        self.acc_num=acc_num
        self.acc_type=acc_type
        self.balance=balance
    
    def information(self):
        print("Your account name is ",self.acc_name, "account number is ",self.acc_num,"account type is ",self.acc_type,"and balance is ", self.balance)

    def deposite(self, balance):
        self.balance = self.balance+balance
        print("Total balance is ",self.balance)

    def withdrawl(self, balance):
        if self.balance < balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance-balance
        
        print("Remaining balance ",self.balance)

user = Banking("Kanchan", 123456, "Fixed", 50000)
user.information()
user.deposite(10000)
user.withdrawl(5000)

