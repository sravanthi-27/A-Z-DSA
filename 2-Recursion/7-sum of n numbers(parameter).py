def fun(i,sum):
    if i<1:
        print(sum)
        return 
    fun(i-1, sum+i)
fun(3,0)