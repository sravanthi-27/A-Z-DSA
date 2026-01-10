i = 1
n = 5
def fun(i,n):
    if n<1:
        return 
    fun(i,n-1)
    print(n)
fun(i,n)
