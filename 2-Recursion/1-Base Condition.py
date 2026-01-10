cnt = 0
def fun(cnt):
    if cnt==3:
        return
    print(cnt)
    cnt += 1
    fun(cnt) 
fun(cnt)
