m=int(input())
n=int(input())
c=[]
for i in range(m,n):
    tmp=int(str(i)[::-1])
    if i==tmp:
        c.append(i)
for i in range(len(c)):
    print(c[i],end=' ')