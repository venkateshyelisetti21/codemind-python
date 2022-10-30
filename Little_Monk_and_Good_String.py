a='aeiou'
b=list(input().lower())
x=0
y=0
for i in range(len(b)):
    if b[i] in a:
        y=0
        for j in range(i,len(b)):
            if b[j] in a:
                y+=1
            else:
                break
    if(x<=y):
        x=y
print(x)