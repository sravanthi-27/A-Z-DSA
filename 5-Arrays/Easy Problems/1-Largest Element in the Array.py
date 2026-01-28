arr = [2,3,1,5,4]
arr.sort()
print(arr[-1])

#optimize
arr = [2,1,6,3,4]
largest = arr[0]
for i in range(1,len(arr)):
    if arr[i]>largest:
        largest = arr[i]
print(largest)