#Brute force
arr = [1,1,1]
cnt = 0
k = 2
for i in range(len(arr)):
    for j in range(i,len(arr)):
        sum = 0
        for r in range(i, j+1):
            sum += arr[r]
        if sum == k:
            cnt += 1
print(cnt)

#Better
arr = [1,1,1]
cnt = 0
k = 2
for i in range(len(arr)):
    sum = 0
    for j in range(i,len(arr)):
        sum += arr[j]
        if sum == k:
            cnt += 1
print(cnt)

#Optimal
arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
k = 3

# Initialize the hashmap
hashmap = {}
hashmap[0] = 1  # Crucial for counting subarrays starting from index 0

cnt = 0
prefix_sum = 0

for num in arr:
    prefix_sum += num
    
    # Logic: If (prefix_sum - k) exists, it means we found a subarray
    remove = prefix_sum - k
    
    if remove in hashmap:
        cnt += hashmap[remove]
    else:
        # We don't add to cnt, but we still need to record the prefix_sum
        pass

    # Update the frequency of the current prefix_sum in the hashmap
    if prefix_sum in hashmap:
        hashmap[prefix_sum] += 1
    else:
        hashmap[prefix_sum] = 1

print(f"Total subarrays: {cnt}")