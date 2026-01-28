arr = [1,1,0,1,1,1,0,1,1]
count = 0
maxi = 0
for i in range(len(arr)):
    if arr[i]==1:
        count+=1
        maxi = max(maxi, count)
    else:
        count=0
print(maxi)