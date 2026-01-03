n = 371
sum = 0
x = n
while n>0:
    lastdigit = n % 10
    sum += lastdigit * lastdigit *lastdigit
    n = n // 10
if x==sum:
    print(True)
else:
    print(False)
    