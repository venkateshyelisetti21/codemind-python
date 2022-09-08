s1=input()
s1=s1.lower()
s2=input()
s2=s2.lower()
c=[]
d=[]
e=[]
for i in range(len(str(s1))):
    if s1[i]!=' ':
        c.append(s1[i])
for i in range(len(str(s2))):
    if s2[i]!=' ':
        d.append(s2[i])
for i in range(len(c)):
    for j in range(len(d)):
        if c[i]==d[j]:
            e.append(c[i])
e=list(set(e))
e.sort()
if len(e):
    for i in range(len(e)):
        print(e[i],end='')
else:
    print(-1)