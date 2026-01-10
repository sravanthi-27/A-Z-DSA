ar = [1, 2, 3, 2, 1]
n0 = 2
cnt = 0
for i in range(len(ar)):
    if ar[i] == n0:
        cnt += 1
print(cnt)