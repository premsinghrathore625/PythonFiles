def check(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not a non-negative integer")

    return helper


n=float(input("enter "))
@check
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
