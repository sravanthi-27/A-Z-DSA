def fun(s,i):
    n = len(s)
    if i>=n//2:
        return True 
    if s[i]!=s[n-i-1]:
        return False 
    return fun(s,i+1)
print(fun("MadaM",0))