'''
Create Account class with 2 attributes - balance & account no.
Create methods for debit, credit & printing the balance.
'''
class Account:

    def __init__(self, bal, acc_no):
        self.bal = bal
        self.acc_no = acc_no

    # Debit method
    def debit(self, ammount):
        self.bal -= ammount
        print(f"Rs. {ammount} was debited")
        print(f"Total balance: {self.get_balance()}")

    # Cradit Method
    def cradit(self, ammount):
        self.bal += ammount
        print(f"Rs. {ammount} was Cradited")
        print(f"Total balance: {self.get_balance()}")
        
    # Balance method
    def get_balance(self):
        return self.bal

u1 = Account(50000, 123456)
print(f"Account no: {u1.acc_no},User Balance: {u1.bal}")
u1.debit(6000)
u1.cradit(1200)
print(u1.get_balance())