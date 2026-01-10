arr = [1,3,2,5,4]
n = len(arr)
for i in range(n-1, 0 , -1):
    didswap = 0
    for j in range(0, i):
        if arr[j]>arr[j+1]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
            didswap=1
    if didswap==0:
        break
print(arr)


