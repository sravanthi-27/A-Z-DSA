cnt = 0 
n = 5
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
if cnt==2:
    print("Prime")
else:
    print("Not a prime number")


# optimize
cnt = 0
for i in range(1, int(n**(1/2))+1):
    if n%i==0:
        cnt+=1
        if n/i!=i:
            cnt+=1
if cnt==2:
    print("Prime")
else:
    print("Not Prime")