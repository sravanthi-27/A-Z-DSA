#Brute force
arr = [2,3,-2,4]
maximum = float('-inf')
for i in range(len(arr)):
    for j in range(i,len(arr)):
        product = 1
        for k in range(i,j+1):
            product *= arr[k]
        maximum = max(maximum, product)
print(maximum)

#better
arr = [2,3,-2,4]
maximum = float('-inf')
for i in range(len(arr)):
    product =1
    for j in range(i,len(arr)):
        product *= arr[j]
        maximum = max(maximum,product)
print(maximum)

#Optimal
arr = [2,3,-2,4]
maxi = float('-inf')
prefix, suffix = 1, 1
n = len(arr)
for i in range(len(arr)):
    if prefix==0:
        prefix = 1 
    if suffix==0:
        suffix=1
    prefix *= arr[i]
    suffix *= arr[n-i-1]
    maxi = max(maxi, max(prefix,suffix))