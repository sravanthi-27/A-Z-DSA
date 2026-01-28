#Brute force
arr = [1,2,3,1,1,1,1,4,2,3]
n = len(arr)
target = 3
max_len = 0
for i in range(n):
    for j in range(i,n):
        curr_sum = 0
        for k in range(i,j+1):
            curr_sum += arr[k]
        if curr_sum == target:
            max_len = max(max_len, j-i+1)
print(max_len)

#Optimal
arr = [1,2,3,1,1,1,1,4,2,3]
n = len(arr)
max_len = 0
for i in range(n):
    curr_sum = 0
    for j in range(i,n):
        curr_sum += arr[j]
        if curr_sum==target:
            max_len = max(max_len, j-i+1)
print(max_len)

#More optimal
arr = [2,0,0,3]
n = len(arr)
max_len = 0
prefix_sum = 0
hashmap = {}
k = 3
for i in range(n):
    prefix_sum += arr[i]
    if prefix_sum == k:
        max_len = max(max_len, i+1)
    remainder = prefix_sum - k 
    if remainder in hashmap:
        length = i-hashmap[remainder]
        max_len = max(max_len, length)
    if prefix_sum not in hashmap:
        hashmap[prefix_sum] = i 
print(max_len)


#More optimal-2 pointer approach
arr = [2,0,0,3]
n = len(arr)
max_len = 0
left = 0
curr_sum = arr[0]
right = 0
while right < n:
    while left<=right and curr_sum>k:
        curr_sum -= arr[left]
        left += 1
    if curr_sum == k:
        max_len = max(max_len, right-left+1)
    right += 1
    if right<n:
        curr_sum += arr[right]
print(max_len)

