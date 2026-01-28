arr = [-1,2,3,4,-3,1]
n = len(arr)
pos , neg = [], []
for i in range(len(arr)):
    if arr[i]<0:
        neg.append(arr[i])
    else:
        pos.append(arr[i])
if len(pos)>len(neg):
    for i in range(len(neg)):
        arr[2*i] = pos[i]
        arr[2*i+1] = neg[i]
    index = len(neg)*2
    for i in range(len(neg),len(pos)):
        arr[index] = pos[i]
        index += 1
else:
    for i in range(len(pos)):
        arr[2*i] = pos[i]
        arr[2*i+1] = neg[i]
    index = len(pos)*2
    for i in range(len(pos),len(neg)):
        arr[index] = neg[i]
        index += 1
print(arr)