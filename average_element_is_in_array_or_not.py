n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    s+=a[i]
avg=int(s/n)
if avg in a:
    print(True)
else:
    print(False)
