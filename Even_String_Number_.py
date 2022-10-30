x=list(input())
a=[]
b=[]
for i in x:
    if i>='0' and i<='9':
        if int(i)%2==0:
            a.append(i)
        else:
            b.append(i)
if len(a):
    a=list(sorted(set(a)))
    b=list(sorted(set(b)))
    tmp=a[0]
    a.remove(tmp)
    c=list(reversed(sorted(a+b)))
    c.append(tmp)
    print(*c,sep='')
else:print(-1)