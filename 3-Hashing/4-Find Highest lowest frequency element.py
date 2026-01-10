arr = [1,1,1,2,3,2]
maxi = 0
mini = float('inf')
di = {}
for i in range(len(arr)):
    if arr[i] not in di:
        di[arr[i]] = 1
    else:
        di[arr[i]] += 1
maxi = max(di.values())
mini = min(di.values())

print(maxi, mini)   