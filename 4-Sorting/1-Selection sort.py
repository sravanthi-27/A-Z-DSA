arr = [3,4,2,6,1]
for i in range(len(arr)-1):
    mini = i 
    for j in range(i+1,len(arr)):
        if arr[j] < arr[mini]:
            mini = j 
    arr[i], arr[mini] = arr[mini], arr[i]
print(arr)

