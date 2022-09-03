n=input()
c=[]
d=[]
for i in range(len(n)):
    if n[i]=='z':
        c.append(n[i])
    elif n[i]=='o':
        d.append(n[i])
if len(d)==(len(c)*2):
    print('Yes')
else:
    print('No')