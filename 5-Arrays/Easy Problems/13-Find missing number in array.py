#Brute force
arr = [1,2,4,5]
for i in range(1,len(arr)+1):
    if i not in arr:
        print(i)

#Optimal
arr = [1,2,4,5]
n = 5
hash = [0]*(n+1)
for i in range(1,n+1):
    if i in arr:
        hash[i]=1
for i in range(1,len(hash)):
    if hash[i]==0:
        print(i)

#More optimal
arr = [1,2,4,5]
n=5
sum = 0
for i in range(len(arr)):
    sum+=arr[i]
sumofn = (n*(n+1))/2
ans = int(sumofn-sum)
print(ans)

#More optimal
arr = [1,2,4,5]
n=5
xor1 = 0
for i in range(1,n+1):
    xor1 = xor1^i 
xor2=0
for i in range(n-1):
    xor2 = xor2^arr[i]
print(xor1^xor2)