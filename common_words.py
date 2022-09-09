s1=input()
s1=s1.lower()
s2=input()
s2=s2.lower()
s1=s1.split()
s2=s2.split()
e=[]
f=[]
g=[]
for i in s1:
    e.append(i)
for j in s2:
    f.append(j)
for j in s2:
    if j in e:
        g.append(j)
print(*g)