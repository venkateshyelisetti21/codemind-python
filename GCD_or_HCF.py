a,b=map(int,input().split())
c=[]
d=[]
e=[]
for i in range(1,a+1):
    if a%i==0:
        c.append(i)
for i in range(1,b+1):
    if b%i==0:
        d.append(i)  
for i in d:
    if i in c:
        e.append(i)
print(max(e))