#Brute force
arr = [2,6,5,8,11]
target = 14
for i in range(len(arr)):
    for j in range(i+1, len(arr)): 
        if arr[i]+arr[j] == target:
            print(i, j)

#Optimal
arr = [2,6,5,8,11]
target = 14
di = {}
for i in range(len(arr)):
    diff = target - arr[i]
    if diff in di:
        print(i, di[diff])
    else:
        di[arr[i]] = i 

#optimal when ans is yes or no only
arr = [2,6,5,8,11]
arr.sort()
left, right = 0, len(arr)-1
ans = False
target = 14
while left<right:
    summation = arr[left]+arr[right]
    if summation==target:
        ans = True
        break
    elif summation<target:
        left += 1
    else:
        right -= 1
print(ans)
    