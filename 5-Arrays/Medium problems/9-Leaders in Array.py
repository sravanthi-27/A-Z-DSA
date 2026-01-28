#Brute force
arr = [10, 22, 12, 3, 0, 6]
leaders = []
for i in range(len(arr)):
    leader = True
    for j in range(i+1, len(arr)):
        if arr[j]>arr[i]:
            leader = False
    if leader==True:
        leaders.append(arr[i])
print(leaders)

#Optimal
arr = [10, 22, 12, 3, 0, 6]
maxi = float('-inf')
leaders = []
for i in range(-1,-len(arr),-1):
    if arr[i] > maxi:
        maxi = arr[i]
        leaders.append(arr[i])
leaders.sort()
print(leaders)