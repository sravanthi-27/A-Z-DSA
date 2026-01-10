arr = [1, 2, 3, 2, 1]
di = {}
for i in range(len(arr)):
    if arr[i] not in di:
        di[arr[i]] = 1
    else:
        di[arr[i]]+=1
num = 3
print(di[3])