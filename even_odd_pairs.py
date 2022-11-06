n=int(input())
m=list(map(int,input().split()))
a=[]
b=[]
c=[]
d=0
for i in range(len(m)):
    if m[i]%2==0:
        a.append(m[i])
    else:
        b.append(m[i])
e=min(len(a),len(b))
if len(a)>len(b):
    f=a
else:
    f=b
while d<len(f):
    if d<e:
        c.append(a[d])
        c.append(b[d])
    else:
        c.append(f[d])
    d+=1
if n%2:
    c.append(0)
print(*c)