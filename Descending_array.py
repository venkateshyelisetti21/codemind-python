n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(n):
    c.append(a[i])
c.sort()
c.reverse()
if c==a:
    print('yes')
else:
    print('no')