s=input()
a=[]
b=[]
c=[]
for i in s:
    if i not in a:
        a.append(i)
    else:b.append(i)
for i in a:
    if i not in b:
        c.append(i)
d=''
for i in c:
   d=i
   break
tmp=-1
for i in range(len(s)):
    if d==s[i]:
        tmp=i
        break
if tmp!=-1:
    print(tmp)
else:print(tmp)