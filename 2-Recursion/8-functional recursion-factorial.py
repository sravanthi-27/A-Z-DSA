#Factorial
def fun(n):
    if n==0:
        return 1
    return n*fun(n-1)
print(fun(5))