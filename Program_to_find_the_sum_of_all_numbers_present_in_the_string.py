n=input()
c=[]
a=10
for i in range(len(n)):
    for j in range(a):
        if n[i]==str(j):
            c.append(n[i])
s=0
for i in range(len(c)):
    s+=int(c[i])
print(s)
    