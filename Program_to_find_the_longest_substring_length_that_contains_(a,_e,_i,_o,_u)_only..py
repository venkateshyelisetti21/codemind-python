a='aeiou'
s=list(input().lower())
x=y=0
for i in range(len(s)):
    if s[i] in a:
        y=0
        for j in range(i,len(s)):
            if s[j] in a:
                y+=1
            else:
                break
        if x<=y:
            x=y
print(x)