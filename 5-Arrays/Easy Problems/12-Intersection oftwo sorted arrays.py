#Brute force
a = [1,2,2,3,3,4,5,6]
b = [2,3,3,5,6,6,7]
visited = [0]*len(b)
res = []
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j] and visited[j]==0:
            visited[j] = 1 
            res.append(b[j])
            break #to stop a[i] checking again
print(res)

#Optimize
a = [1,2,2,3,3,4,5,6]
b = [2,3,3,5,6,6,7]
n, m = len(a), len(b)
i , j = 0, 0
res = []
while i<n and j<m:
    if a[i]<b[j]:
        i+=1
    elif b[j]<a[i]:
        j+=1
    else:
        res.append(a[i])
        i+=1
        j+=1
print(res)