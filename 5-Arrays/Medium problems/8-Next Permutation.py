arr = [2, 3, 5, 4, 1, 0, 0]
index = -1
n = len(arr)

# 1. Find the break point (pivot)
for i in range(n - 2, -1, -1): # Start from n-2 to check i and i+1
    if arr[i] < arr[i+1]:
        index = i
        break 

# 2. If no break point, the array is in descending order, so reverse it all
if index == -1:
    arr.reverse()
else:
    # 3. Find the next largest number to swap with the pivot
    for i in range(n - 1, index, -1):
        if arr[i] > arr[index]:
            arr[index], arr[i] = arr[i], arr[index]
            break

    # 4. Reverse the suffix (everything to the right of index)
    # This is the "reverse code" you were looking for:
    left = index + 1
    right = n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

print(arr) # Output: [2, 4, 0, 0, 1, 3, 5]