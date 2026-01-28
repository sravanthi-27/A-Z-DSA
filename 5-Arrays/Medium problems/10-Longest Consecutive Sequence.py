#Brute Force
arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]
longest = 1
for i in range(len(arr)):
    x = arr[i]
    cnt = 1
    x += 1
    while x in arr:
        x += 1
        cnt += 1
    longest = max(longest, cnt)
print(longest)

#Better solution
arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]
arr.sort()
lastsmaller = float('-inf')
longest = 1
cnt = 0
for i in range(len(arr)):
    if arr[i]-1 == lastsmaller:
        cnt += 1
        lastsmaller = arr[i]
    elif arr[i]!=lastsmaller:
        cnt = 1
        lastsmaller = arr[i] 
    longest = max(longest, cnt)
print(longest)

#Optimal
def longestConsecutive(nums):
    if not nums:
        return 0
    
    # Convert list to set for O(1) lookups
    st = set(nums)
    longest = 0
    
    for x in st:
        # Check if 'x' is the start of a sequence
        if (x - 1) not in st:
            # This is a starting point
            cnt = 1
            current_num = x
            
            # Check for consecutive elements
            while (current_num + 1) in st:
                current_num += 1
                cnt += 1
            
            longest = max(longest, cnt)
            
    return longest

# Example usage:
arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]
print(f"Longest consecutive sequence length: {longestConsecutive(arr)}")

