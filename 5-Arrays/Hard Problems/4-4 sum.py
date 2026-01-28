#Brute force
arr = [1,0,-1,0,-2,2]
target = 0
n = len(arr)
sets = set()
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            for l in range(k+1,n):
                temp = arr[i]+arr[j]+arr[k]+arr[l]
                if temp == target:
                    arrs = [arr[i],arr[j],arr[k],arr[l]]
                    arrs.sort()
                    sets.add(tuple(arrs))
res = [list(t) for t in sets]
print(res)

#Better
arr = [1,0,-1,0,-2,2]
target = 0
n = len(arr)
sets = set()
for i in range(n):
    for j in range(i+1,n):
        li = set()
        for k in range(j+1,n):
            temp = target - (arr[i]+arr[j]+arr[k])
            if temp in li:
                arrs = [arr[i],arr[j],arr[k],temp]
                arrs.sort()
                sets.add(tuple(arrs))
            else:
                li.add(arr[k])
res = [list(t) for t in sets]
print(res)

#Optimal
arr = [1, 0, -1, 0, -2, 2]
arr.sort()
target = 0
n = len(arr)
res = []
for i in range(n):
    if i>0 and arr[i] == arr[i-1]:
        continue 
    for j in range(i+1, n):
        if j != i+1 and arr[j] == arr[j-1]:
            continue
        k = j+1
        l = n-1
        while k < l:
            temp = arr[i]+arr[j]+arr[k]+arr[l]
            if temp < target:
                k += 1
            elif temp > target:
                l -= 1
            else:
                res.append([arr[i],arr[j],arr[k],arr[l]])
                k += 1
                l -= 1
                while k < l and arr[k] == arr[k-1]:
                    k += 1
                while k < l and arr[l] == arr[l+1]:
                    l -= 1
print(res)
            
