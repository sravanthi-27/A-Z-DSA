#brute force
arr1 = [1,1,2,3,4,5]
arr2 = [2,3,4,5,5,6]
union = set()
for x in arr1:
    union.add(x)
for x in arr2:
    union.add(x)
result = sorted(union)
print(result)
     

#optimize
arr1 = [1,1,2,3,4,5]
arr2 = [2,3,4,5,5,6]

i = j = 0
n, m = len(arr1), len(arr2)
union = []

while i < n and j < m:
    if arr1[i] == arr2[j]:
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
        j += 1

    elif arr1[i] < arr2[j]:
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    else:
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

while i < n:
    if not union or union[-1] != arr1[i]:
        union.append(arr1[i])
    i += 1

while j < m:
    if not union or union[-1] != arr2[j]:
        union.append(arr2[j])
    j += 1

print(union)
