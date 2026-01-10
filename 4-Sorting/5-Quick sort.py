def partition(arr,low,high):
    pivot = low
    i = low
    j = high 
    while(i<j):
        while arr[i]<=arr[pivot] and i<=high-1:
            i+=1
        while arr[j]>arr[pivot] and j >= low+1:
            j-=1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[pivot] = arr[pivot], arr[j]
    return j
def quicksort(arr,low,high):
    if low<high:  #checking if arr has more than one element
        pindex = partition(arr, low, high)
        quicksort(arr, low, pindex-1)
        quicksort(arr, pindex+1, high)
    return arr

print(quicksort([4,3,2,1,8],0,4))

 