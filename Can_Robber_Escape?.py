a=int(input())
b=0
c=list(map(int,input().split()))
for i in range(a):
    if c[i]%2!=0:
        b+=1
if b<=2:print('YES')
else:print('NO')