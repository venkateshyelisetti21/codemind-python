a=int(input())
b=[]
c=0
for i in range(a):
    d=int(input())
    b.append(d)
e=int(input())
for i in b:
    if i<=e:
        c+=1
    else:
        c+=2
print(c)