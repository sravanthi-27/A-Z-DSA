arr = [3,4,5,1,2]
count = 0
ans = True
for i in range(len(arr)):
    if arr[i]>arr[(i+1)%len(arr)]:
        count+=1
    if count>1:
        ans = False 
        break 
print(ans)
