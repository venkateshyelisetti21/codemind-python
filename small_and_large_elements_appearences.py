n=input()
a=[]
for i in n:
    if i!=' ':a.append(i)
b=min(a)
c=max(a)
d=[]
e=[]
for i in a:
    if i==b:d.append(i)
for i in a:
    if i==c:e.append(i)
print(b,len(d),c,len(e))