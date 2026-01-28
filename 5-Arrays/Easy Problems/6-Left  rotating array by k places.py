#Brute force
arr = [1,2,3,4,5]
k = 7
n = len(arr)
k = k%n 
temp = [0]*k
for i in range(k):
    temp[i] = arr[i] 
for i in range(k,n):
    arr[i-k] = arr[i]
for i in range(n-k, n):
    arr[i] = temp[i-(n-k)]
print(arr)

#Optimize
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def leftRotate(arr, k):
    n = len(arr)
    k %= n

    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    reverse(arr, 0, n-1)


arr = [1,2,3,4,5]
leftRotate(arr, 2)
print(arr)

