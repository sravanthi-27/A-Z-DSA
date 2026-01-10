n = int(input("Enter a number:"))
name = input("enter name:")
cnt = 0
def fun(n, name, cnt):
    if cnt>=n:
        return 
    print(name)
    cnt +=1
    fun(n, name, cnt)
fun(n, name, cnt)