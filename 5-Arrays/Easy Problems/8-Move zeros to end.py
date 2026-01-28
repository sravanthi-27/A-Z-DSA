#Brute force
arr = [1,0,2,3,2,0,0,4,5,1]
temp = []
arrsize = len(arr)
for i in range(len(arr)):
    if arr[i]!=0:
        temp.append(arr[i])
for i in range(len(temp)):
    arr[i] = temp[i]
tempsize = len(temp)
for i in range(tempsize,arrsize):
    arr[i] = 0
print(arr)

#opitmal
arr = [1,0,2,3,2,0,0,4,5,1]
j = -1
for i in range(len(arr)):
    if arr[i]==0:
        j = i 
        break
print(j) 
if j==-1:
    print(arr)
else:
    for i in range(j+1,len(arr)):
        if arr[i]!=0:
            arr[j], arr[i] = arr[i], arr[j]
            j+=1    
print(arr)