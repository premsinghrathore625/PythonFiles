class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def show(self):
        print(self.real,"i +",self.img,"j")
    def __add__(self,num2):
        newreal= self.real + num2.real
        newimg= self.img + num2.img
        
        return complex(newreal,newimg)
    
    
num1=complex(1,2)
num2=complex(3,4)
num1.show()
num2.show()
num3= num1 + (num2)
num3.show()  

# we want to do simply + operation in num1 and num2 we need to make dunder function 
# that is instead of add() we will use __add__()          