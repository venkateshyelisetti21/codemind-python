n=int(input())
a=list(map(int,input().split()))
s1=0
s2=0
for i in range(n):
    if i%2==0:
        s1+=a[i]
    else:
        s2+=a[i]
print(s1-s2)