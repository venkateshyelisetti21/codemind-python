n=int(input())
sum=0
for i in range(0,n):
    sum=i*(i+1)
    if sum==n:
        break
if sum==n:
    print('YES')
else:
    print('NO')