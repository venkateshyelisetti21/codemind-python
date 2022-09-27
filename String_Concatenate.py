a=input()
b=input()
c=[]
for i in a:
    c.append(i)
for i in b:
    c.append(i)
c.sort()
for i in c:
    print(i,end='')