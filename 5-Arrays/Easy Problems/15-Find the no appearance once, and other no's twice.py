#Brute force
arr = [1,1,2,3,3,4,4]
for i in range(len(arr)):
    cnt = 0
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            cnt+=1
    if cnt==1:
        print(arr[i])

#Optimal
arr = [1,1,2,3,3,4,4]
maxi = arr[0]
n = len(arr)
for i in range(n):
    maxi = max(maxi, arr[i])
hash = [0]*(maxi+1) 
for i in range(n):
    hash[arr[i]]+=1
for i in range(n):
    if hash[arr[i]]==1:
        print(arr[i])

#More optimal
arr = [1,1,2,3,3,4,4]
xor = 0
for i in range(len(arr)):
    xor ^= arr[i]
print(xor)