count = 0
n = 1234
while n>0:
    lastdigit = n%10
    n = n//10
    count += 1
print(count)