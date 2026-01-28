#Brute force
arr = [3,1,-2,-5,2,-4]
pos = []
neg = []
for i in range(len(arr)):
    if arr[i]>0:
        pos.append(arr[i])
    else:
        neg.append(arr[i])
for i in range(len(arr)//2):
    arr[2*i] = pos[i]
    arr[2*i+1] = neg[i]
print(arr)

#Optimal
arr = [3,1,-2,-5,2,-4]
n = len(arr)
res = [0]*n
posIndex, negIndex = 0, 1
for i in range(n):
    if arr[i]>0:
        res[posIndex] = arr[i]
        posIndex += 2
    else:
        res[negIndex] = arr[i]
        negIndex += 2
print(res)