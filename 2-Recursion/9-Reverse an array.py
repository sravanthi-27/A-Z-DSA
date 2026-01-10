#two pointers
a = [1,2,3,4,5]
l = 0
r = len(a)-1
def fun(a,l,r):
    if l>=r:
        print(a)
        return
    a[l], a[r] = a[r], a[l]
    l+=1
    r-=1
    fun(a,l,r)
fun(a,l,r)

#using single pointer
b = [1,2,3,4,5]
i = 0 
def fun(b,i):
    n = len(b)
    if i>=len(b)//2:
        print(b)
        return 
    b[i], b[n-i-1] = b[n-i-1], b[i]
    i += 1
    fun(b,i)
fun(b,i)