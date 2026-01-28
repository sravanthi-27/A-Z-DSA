#Brute force
arr = [2,2,3,3,1,2,2]
n = len(arr)
times = n//2
for i in range(len(arr)):
    cnt = 0
    for j in range(len(arr)):
        if arr[j]==arr[i]:
            cnt +=1
    if cnt > times:
        print(arr[i])

#Optimal
arr = [2,2,3,3,1,2,2]
n = len(arr)
times = n//2
di = {}
for i in range(len(arr)):
    if arr[i] not in di:
        di[arr[i]]=1
    else:
        di[arr[i]]+=1
for cnt in di:
    if di[cnt]>times:
        print(cnt)

#More optimal
arr = [2,2,3,3,3,2]
n = len(arr)
times = n//2
cnt = 0
for i in range(n):
    if cnt==0:
        element = arr[i]
        cnt = 1
    elif arr[i]==element:
        cnt += 1
    else:
        cnt -=1 
print(element)