n=int(input())
m=list(map(int,input().split()))
s=len(m)
for i in range(len(m)//2):
    print(m[i],m[(s)-1],end=' ')
    s-=1
if len(m)%2: print(m[n//2],0)