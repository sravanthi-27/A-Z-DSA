#Brute force
arr = [40, 25, 19, 12, 9, 6, 2]
cnt = 0
n = len(arr)
for i in range(n):
    for j in range(i+1, n):
        if arr[i] > 2*arr[j]:
            cnt += 1
print(cnt)

#Optimal
arr = [40, 25, 19, 12, 9, 6, 2]
n = len(arr)

def countpairs(arr, low, mid, high):
    right = mid+1
    cnt = 0
    for i in range(low, mid+1):
        while right <= high and arr[i] > 2* arr[right]:
            right += 1
        cnt += right-(mid+1)
    return cnt
def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def mergeSort(arr, low, high):
    cnt = 0
    if low >= high:
        return

    mid = (low + high) // 2
    cnt+=mergeSort(arr, low, mid)
    cnt+=mergeSort(arr, mid + 1, high)
    cnt += countpairs(arr, low, mid, high)
    merge(arr, low, mid, high)   # 👈 HERE
    return cnt


arr = [3, 2, 4, 1, 3]
mergeSort(arr, 0, len(arr) - 1)
print(cnt)

