#Brute force
def markrow(i, m, matrix):
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def markcol(j, n, matrix):
    # Use 'r' for row index to avoid confusing it with 'j' (column)
    for r in range(n): 
        if matrix[r][j] != 0:
            matrix[r][j] = -1

matrix = [[1,1,1],[1,0,1],[1,1,1]]
n = len(matrix)
m = len(matrix[0])

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            markrow(i, m, matrix)
            markcol(j, n, matrix)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == -1:
            matrix[i][j] = 0

print(matrix)

#Better
matrix = [[1,1,1],[1,0,1],[1,1,1]]
n = len(matrix)
m = len(matrix[0])
col = [0]*m
row = [0]*n 
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            row[i] = 1 
            col[j] = 1
for i in range(n):
    for j in range(m):
        if row[i] == 1 or col[j] == 1:
            matrix[i][j] = 0
print(matrix)

#Optimal
matrix = [[1,1,1],[1,0,1],[1,1,1]]
n = len(matrix)
m = len(matrix[0])
col0 = matrix[0][0]
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            #Mark the ith row
            matrix[i][0] = 0
            #Mark the jth column
            if j!=0:  #bcz we can't change 1st element
                matrix[0][j] = 0
            else:
                col0 = 0
for i in range(1,n):
    for j in range(1,m):
        if matrix[i][j]!=0:
            if matrix[0][j]==0 or matrix[i][0] == 0:
                matrix[i][j] = 0
if matrix[0][0]==0:
    for i in range(m):
        matrix[0][i]=0
if col0 == 0:
    for i in range(n):
        matrix[i][0] = 0
print(matrix)