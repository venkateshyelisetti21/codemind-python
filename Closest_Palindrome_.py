n=int(input())
a=n
tmp=0
while True:
    a+=1
    rev=int(str(a)[::-1])
    if a==rev:
      tmp=a
      break
    else:continue
b=n
tmp1=0
while True:
    b-=1
    rev=int(str(b)[::-1])
    if b==rev:
      tmp1=b
      break
    else:continue
x=abs(n-tmp)
y=abs(n-tmp1)
if x!=y:
    print(min(tmp1,tmp))
else:print(tmp1,tmp)