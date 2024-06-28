import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func.__name__ +"took" + str((end-start)*1000)+"milsec")
        return result
    return wrapper

@time_it
def square(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
    return result    
