n=int(input())
c=[]
d=[]
for i in range(n+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            c.append(i)
for i in range(1,n+1):
    if n%i==0:
        if i not in c:
            d.append(i)
print(len(d))