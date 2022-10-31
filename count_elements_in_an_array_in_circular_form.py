n=int(input())
a=list(map(int,input().split()))
b=a+a
ctr=0
for i in range(n):
    if (b[i]%2!=0 and b[i+2]%2==0) or (b[i]%2==0 and b[i+2]%2!=0):
        ctr+=1
print(ctr)