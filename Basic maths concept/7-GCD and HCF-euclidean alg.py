#Brute force
n1=12
n2=9
for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
        gcd = i
print(gcd)

#optimize
for i in range(min(n1,n2),0,-1):
    if n1%i==0 and n2%i==0:
        gcd=i
        break
print(gcd)

#Euclidean algorithm
a, b = 20, 40
while a>0 and b>0:
    if a>b:
        a=a%b 
    else:
        b=b%a 
if a==0:
    print(b)
else:
    print(a)