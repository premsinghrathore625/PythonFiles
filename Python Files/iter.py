def fib(n):
    if(n==1 or n==2):
        return n-1
    
    return fib(n-1)+fib(n-2)


arr=[]
x=int(input("enter number"))
for i in range(1,x+1):
    arr.append(fib(i))
    
itr=iter(arr)
print(next(itr))    