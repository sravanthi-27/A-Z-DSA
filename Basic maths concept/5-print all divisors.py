n = 36
for i in range(1, n+1):
    if n%i ==0 :
        #print(i)
        pass

#optimize
arr = []
for i in range(1, int((n)**(1/2))+1):
    if n%i==0:
        arr.append(i)
        if (n/i!=i):
            arr.append(int(n/i))
print(arr)