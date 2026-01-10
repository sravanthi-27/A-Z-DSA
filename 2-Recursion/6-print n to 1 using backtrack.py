i = 1
n = 5
def fun(i,n):
    if i>n:
        return 
    print(i)
    fun(i+1,n)
fun(i,n)