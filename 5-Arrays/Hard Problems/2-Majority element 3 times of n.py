#Brute force
arr = [1,1,1,3,3,2,2,2]
ans = []
majority = len(arr) // 3
for i in range(len(arr)):
    cnt = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            cnt += 1
    if cnt > majority and arr[i] not in ans:
        ans.append(arr[i])
print(ans)

#Better
arr = [1,1,1,3,3,2,2,2]
ans = []
di = {}
majority = len(arr) // 3
for i in range(len(arr)):
    if arr[i] not in di:
        di[arr[i]] = 1
    else:
        di[arr[i]] += 1
        if di[arr[i]] > majority:
            ans.append(arr[i])
print(ans)

#Optimal
arr = [1,1,1,3,3,2,2,2]
ans = []
majority = len(arr) // 3
cnt1, cnt2 = 0, 0
element1, element2 = None, None
for i in range(len(arr)):
    if cnt1 == 0 and arr[i]!=element2:
        cnt1 = 1
        element1 = arr[i]
    elif cnt2 == 0 and arr[i]!=element1:
        cnt2 = 1
        element2 = arr[i]
    elif element1==arr[i]:
        cnt1 += 1
    elif element2 == arr[i]:
        cnt2 += 1
    else:
        cnt1-=1
        cnt2-=1
cnt1, cnt2 = 0, 0
for i in range(len(arr)):
    if arr[i] == element1:
        cnt1+=1
    if arr[i]==element2:
        cnt2 += 1
if cnt1 > majority:
    ans.append(element1)
if cnt2 > majority:
    ans.append(element2)
print(ans)