i=1
n=5
def fun(i,n):
    if i>n:
        return 
    print(i)
    i+=1
    fun(i,n)
fun(i,n)
