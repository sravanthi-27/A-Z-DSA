#Brute force
arr = [0,1,2,0,1,2,1,2,0,0,0,1]
cnt0, cnt1, cnt2 = 0, 0, 0
for i in range(len(arr)):
    if arr[i]==0:
        cnt0 += 1
    elif arr[i]==1:
        cnt1 += 1
    else:
        cnt2+=1
for i in range(cnt0):
    arr[i] = 0
for i in range(cnt0, cnt0+cnt1):
    arr[i]=1
for i in range(cnt0+cnt1, len(arr)):
    arr[i] = 2
print(arr)

#Optimal
arr = [0,1,2,0,1,2,1,2,0,0,0,1]
low = 0
mid = 0
high = len(arr)-1
while mid <= high :
    if arr[mid] == 0:
        arr[low], arr[mid] = arr[mid], arr[low]
        low+=1
        mid+=1
    elif arr[mid]==1:
        mid += 1
    else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1
print(arr)