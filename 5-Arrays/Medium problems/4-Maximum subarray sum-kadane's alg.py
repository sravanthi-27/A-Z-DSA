#Brute force
arr = [-2,-3,4,-1,-2,1,5,-3]
maxi = float('-inf')
for i in range(len(arr)):
    for j in range(i,len(arr)):
        summation = 0
        for k in range(i,j):
            summation += arr[k]
        maxi = max(summation, maxi)
print(maxi)

#Better sol
arr = [-2,-3,4,-1,-2,1,5,-3]
maxi = float('-inf')
for i in range(len(arr)):
    summation = 0
    for j in range(i,len(arr)):
        summation += arr[j]
        maxi = max(maxi, summation)
print(maxi)

#Optimal
arr = [-2,-3,4,-1,-2,1,5,-3]
maxi = float('-inf')
summation = 0
for i in range(len(arr)):
    summation += arr[i]
    maxi = max(maxi,summation)
    if summation<0:
        summation = 0
if maxi<0:
    print(-1)
print(maxi)

#to print that subarray
arr = [-2,-3,4,-1,-2,1,5,-3]
maxi = float('-inf')
summation = 0
for i in range(len(arr)):
    if summation == 0:
        start = i 
    summation += arr[i]
    if summation > maxi:
        maxi = summation
        ans_start = start 
        ans_end = i
    if summation<0:
        summation = 0
if maxi<0:
    print(-1)
print(maxi)
print(arr[ans_start:ans_end+1])