s1=input()
s1=s1.lower()
s2=input()
s2=s2.lower()
s1=s1.split()
s2=s2.split()
a=[]
b=[]
c=[]
for i in s1:
    a.append(i)
for j in s2:
    b.append(j)
for j in s2:
    if j in a:
        c.append(j)
print(len(c))