class Account:
    def __init__(self,account_no,balance) :
        self.account_no= account_no
        self.balance= balance
        
    def debit(self,amount):
        self.balance-=amount
        print(amount,"is debited")
        
    def credit(self,amt) :
        self.balance+=amt
        print(amt,"is credited")  
        
    def get_balance(self):
        print(self.balance)     

a1=Account(456,500) 
print(a1.balance,a1.account_no)

a1.credit(100)
a1.debit(300)
a1.get_balance()   
    
       