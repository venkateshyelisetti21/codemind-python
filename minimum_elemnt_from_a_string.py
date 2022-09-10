n=input()
n=n.split()
c=[]
tmp=0
for i in n:
   tmp=i 
for i in tmp:
    c.append(i)
tmp=min(c)
tmp1=tmp.lower()
if tmp1 in c:
    print(tmp1)
else:print(tmp)