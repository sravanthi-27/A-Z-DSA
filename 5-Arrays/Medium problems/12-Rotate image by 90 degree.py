#Brute force
matrix = [[1,2,3],[4,5,6],[7,8,9]]
n = len(matrix)
m = len(matrix[0])
ans = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        ans[j][n-i-1] = matrix[i][j]
print(ans)

#Optimal
matrix = [[1,2,3],[4,5,6],[7,8,9]]
n = len(matrix)
m = len(matrix[0])
for i in range(n):
    for j in range(i+1,n):
        matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
for i in range(n):
    matrix[i].reverse()
print(matrix)