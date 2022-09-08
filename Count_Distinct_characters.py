n=input()
n=n.lower()
c=[]
for i in range(len(str(n))):
    if n[i]!=' ':
        if n[i] not in c:
            c.append(n[i])
print(len(c))