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
    if c[i]not in d:
        e.append(c[i])
for i in range(len(d)):
    if d[i]not in c:
        e.append(d[i])
e=list(set(e))
print(len(e))