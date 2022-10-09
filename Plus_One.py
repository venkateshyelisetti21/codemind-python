n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s+=i*(10**(n-1))
    n-=1
s+=1
c=[]
while s:
    r=s%10
    c.append(r)
    s//=10
c.reverse()
print(*c)