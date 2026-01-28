#Brute force
arr1 = [1,3,5,7]
arr2 = [0,2,6,8,9]
n, m = len(arr1), len(arr2)
res = []
left = 0
right = 0

while left < n and right < m:
    if arr1[left] <= arr2[right]:
        res.append(arr1[left])
        left += 1
    else:
        res.append(arr2[right])
        right += 1
while left < n:
    res.append(arr1[left])
    left += 1
while right < m:
    res.append(arr2[right])
    right += 1
print(res)
for i in range(len(res)):
    if i<n:
        arr1[i] = res[i]
    else:
        arr2[i-n] = res[i]
print(arr1,arr2)

#optimal1
arr1 = [1,3,5,7]
arr2 = [0,2,6,8,9]
n, m = len(arr1), len(arr2)
left = n-1
right = 0
while left>=0 and right < m:
    if arr2[right] < arr1[left]:
        arr2[right], arr1[left] = arr1[left], arr2[right]
        left -=1
        right += 1
    else:
        break
arr2.sort()
arr1.sort()
print(arr1, arr2)

#optimal2
arr1 = [1,3,5,7]
arr2 = [0,2,6,8,9]
n, m = len(arr1), len(arr2)
length = n+m 
gap = (length//2) + (length%2)
def swap(arr1, arr2, index1, index2):
    if arr1[index1] > arr2[index2]:
        arr1[index1], arr2[index2] = arr2[index2], arr1[index1]
while gap>0:
    left = 0
    right = left + gap 
    while right < length:
        #both arr1 and arr2
        if left < n and right >= n:
            swap(arr1,arr2,left,right-n) 
        #arr2 and arr2
        elif left >= n:
            swap(arr2,arr2,left-n,right-n)
        #arr1 and arr1
        else:
            swap(arr1,arr1,left,right)
        left += 1
        right +=1
    if gap==1:
        break
    gap = (gap//2)+(gap%2)
print(arr1,arr2) 