n=int(input())
c=[]
for i in range(1,n+1):
    if n%i==0:
        c.append(i)
x=min(c)
y=max(c)
d=[]
for i in range(x,y):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            d.append(i)
e=[]
for i in range(len(c)):
    if c[i] in d:
        pass
    else:
        e.append(c[i])
print(len(e))