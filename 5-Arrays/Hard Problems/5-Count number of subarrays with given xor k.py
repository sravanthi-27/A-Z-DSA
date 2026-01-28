#Brute force
arr = [4,2,2,6,4]
k = 6
cnt = 0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        xor = 0
        for r in range(i,j+1):
            xor = xor ^ arr[r]
        if xor == k:
            cnt += 1
print(cnt)

#Better
arr = [4,2,2,6,4]
k = 6
cnt = 0
for i in range(len(arr)):
    xor = 0
    for j in range(i, len(arr)):
        xor ^= arr[j]
        if xor == k:
            cnt += 1
print(cnt)

#Optimal
arr = [4,2,2,6,4]
k = 6
cnt = 0
di = {0:1}
xor = 0
for i in range(len(arr)):
    xor ^= arr[i]
    x = xor ^ k
    if x in di:
        cnt += di[x]
    if xor in di:
        di[xor]+=1
    else:
        di[xor]=1
print(cnt)
