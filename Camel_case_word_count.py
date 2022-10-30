def c(s):
    ctr=1
    for i in range(1,len(s)-1):
        if s[i].isupper():
            ctr+=1
    return ctr
s=input()
print(c(s))