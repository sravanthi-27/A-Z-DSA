s = "abcdabefc"
di = {}
for i in range(len(s)):
    val = ord(s[i])-97
    if val not in di:
        di[val] = 1
    else:
        di[val] += 1
print(di)