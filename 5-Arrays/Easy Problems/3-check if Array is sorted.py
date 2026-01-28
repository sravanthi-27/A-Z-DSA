arr = [1,2,3,4,5]
for i in range(1,len(arr)):
    if arr[i]>=arr[i-1]:
        ans = True
    else:
        ans = False
print(ans)