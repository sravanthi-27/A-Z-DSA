arr = [7,1,5,3,6,4]
mini = arr[0]
profit = 0
for i in range(1,len(arr)):
    cost = arr[i]-mini 
    profit = max(cost, profit)
    mini = min(mini, arr[i])
print(profit)