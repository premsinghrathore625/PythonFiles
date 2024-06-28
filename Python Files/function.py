def pattern(num) :
    for i in range (1,num+1) :
        s=""
        for j in range (i):
            s+="*"
        print(s)
        
        
x=int(input("enter number"))
pattern(x)        