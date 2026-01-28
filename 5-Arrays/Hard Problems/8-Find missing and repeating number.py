#Brute force
arr = [4,3,6,2,1,1]
repeating, missing = -1, -1
for i in range(1,len(arr)+1):
    cnt = 0
    for j in range(len(arr)):
        if arr[j] == i:
            cnt += 1
    if cnt == 2:
        repeating = i 
    if cnt ==0 :
        missing = i
print(missing,repeating)

#better
arr = [4,3,6,2,1,1]
repeating, missing = -1, -1
hash_arr = [0]*(len(arr)+1)
for i in range(len(arr)):
    hash_arr[arr[i]] += 1
for i in range(1, len(hash_arr)):
    if hash_arr[i] == 2:
        repeating = i
    elif hash_arr[i] == 0:
        missing = i
print(repeating, missing)

#Optimal-mathematical solution
arr = [4,3,6,2,1,1]
n = len(arr)
sn = (n*(n+1))//2
s2n = (n * (n+1) * (2*n+1)) // 6 
s = 0
s2 = 0
for i in range(n):
    s += arr[i]
    s2 += arr[i]*arr[i]
val1 = s-sn   #x-y
val2 = s2-s2n  
val2 = val2/val1 #x+y
x = int((val1+val2) //2 )
y = x - val1 
print(x,y)

#optimal - xor 
arr = [4,3,6,2,1,1]
n = len(arr)

xr = 0
for i in range(n):
    xr ^= arr[i]
    xr ^= (i+1)

bitno = 0
while ((xr & (1 << bitno)) == 0):
    bitno += 1

zero = 0
one = 0

for i in range(n):
    if (arr[i] & (1 << bitno)) != 0:
        one ^= arr[i]
    else:
        zero ^= arr[i]

for i in range(1, n+1):
    if (i & (1 << bitno)) != 0:
        one ^= i
    else:
        zero ^= i

# check which is repeating
if arr.count(zero) == 2:
    print(zero, one)   # repeating, missing
else:
    print(one, zero)
