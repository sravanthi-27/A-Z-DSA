#Brute force
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort()
n = len(intervals)
res = []
for i in range(n):
    start = intervals[i][0]
    end = intervals[i][1]
    if len(res)!=0 and end <= res[-1][1]:
        continue
    for j in range(i+1,n):
        if intervals[j][0] <= end :
            end = max(end, intervals[j][1])
        else:
            break
    res.append([start,end])
print(res)

#Optimal
#Brute force
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort()
n = len(intervals)
res = []
start = intervals[0][0]
end = intervals[0][1]
for i in range(1, n):
    if intervals[i][0] <= end:
        end = max(end, intervals[i][1])
    else:
        res.append([start, end])
        start, end = intervals[i]
res.append([start,end])
print(res)