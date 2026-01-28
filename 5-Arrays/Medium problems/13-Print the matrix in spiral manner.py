matrix = [[1,2,3],[4,5,6],[7,8,9]]
n = len(matrix)
m = len(matrix[0])
left = 0
right = m-1
bottom = n-1
top = 0
res = []
while top <= bottom and left<= right:
    # Right
    for i in range(left,right+1):
        res.append(matrix[top][i])
    top += 1
    # Bottom
    for i in range(top, bottom+1):
        res.append(matrix[i][right])
    right -= 1
    if(top<= bottom):  #What if there's one row
        #left
        for i in range(right, left-1, -1):
            res.append(matrix[bottom][i])
            print(matrix[bottom][i])
        bottom -= 1
    if left <= right:  #what if there's only one col
        #top
        for i in range(bottom, top-1, -1):
            res.append(matrix[i][left])
        left += 1
print(res)