n = 5
i = 1
def fun(n,i):
    if n<i:
        return 
    print(n)
    n-=1
    fun(n,i)
fun(n,i)
    