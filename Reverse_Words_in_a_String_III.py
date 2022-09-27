n=input()
n=n.split()
c=[]
for i in n:
    tmp=i
    tmp=tmp[::-1]
    c.append(tmp)
print(*c)