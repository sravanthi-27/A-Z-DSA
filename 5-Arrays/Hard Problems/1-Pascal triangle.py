#Type1 question
def fun(row,col):
    n = row - 1
    r = col - 1
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res
print(fun(5,3))

#Type 2 question
#brute force
number_of_rows = 5
for i in range(1, number_of_rows+1):
    print(fun(number_of_rows, i),end=" ")

#optimal
ans = 1
number_of_rows = 6
for i in range(1,number_of_rows):
    ans = ans * (number_of_rows-i)
    ans = ans // i
    print(ans)

#Type 3 question
#Brute force
n = 5
ans = []
for row in range(1,n+1):
    temp = []
    for col in range(1, n+1):
        res = fun(row, col)
        if res != 0:
            temp.append(res)
    ans.append(temp)
print(ans)

#Optimal
def generate_row(n):
    row = [1]
    ans = 1
    for i in range(1, n):
        ans = ans * (n - i)
        ans = ans // i
        row.append(ans)
    return row

n = 5
res = []

for row in range(1, n + 1):
    res.append(generate_row(row))

print(res)

