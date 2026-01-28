#Brute force
arr = [-1, 0, 1, 2, -1, -4]
n = len(arr)
res = []
sets = set()

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i] + arr[j] + arr[k] == 0:
                temp = [arr[i], arr[j], arr[k]]
                temp.sort()
                sets.add(tuple(temp))  # convert list to tuple

res = [list(t) for t in sets]
print(res)

#Better
arr = [-1, 0, 1, 2, -1, -4]
n = len(arr)
sets = set()
for i in range(n):
    li = set()
    for j in range(i+1, n):
        k = -(arr[i]+arr[j])
        if k in li:
            temp = [arr[i], k, arr[j]]
            temp.sort()
            sets.add(tuple(temp))
        else:
            li.add(arr[j])
res = [list(t) for t in sets]
print(res)

#Optimal
arr = [-1, 0, 1, 2, -1, -4]
n = len(arr)
arr.sort()
res = []
for i in range(n):
    if i > 0 and arr[i] == arr[i-1]:
        continue
    j = i+1
    k = n-1
    while j<k:
        temp = arr[i]+arr[j]+arr[k]
        if temp < 0:
            j += 1
        elif temp > 0:
            k -= 1
        else:
            res.extend([[arr[i],arr[j],arr[k]]])
            j += 1
            k -= 1
            while j<k and arr[j] == arr[j-1]:
                j += 1
            while j < k and arr[k] == arr[k+1]:
                k-=1
print(res)
