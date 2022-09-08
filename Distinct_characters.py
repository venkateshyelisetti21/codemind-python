n=input()
n=n.lower()
c=[]
d=[]
e=[]
for i in range(len(str(n))):
    if n[i]!=' ':
        if n[i] not in c:
            c.append(n[i])
        else:
            d.append(n[i])
d=list(set(d))
for i in range(len(c)):
    if c[i] not in d:
        e.append(c[i])
e.sort()
for i in range(len(e)):
    print(e[i],end='')
