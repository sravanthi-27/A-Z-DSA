def fun(n):
    if n<=1:
        return n
    return fun(n-1)+fun(n-2)
print(fun(7))
