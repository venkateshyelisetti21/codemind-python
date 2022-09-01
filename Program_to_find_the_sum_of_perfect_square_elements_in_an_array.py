import math
n=int(input())
a=list(map(int,input().split()))
c=[]
e=[]
sum=0
for i in range(n):
    tmp=math.sqrt(a[i])
    c.append(tmp)
for i in range(len(c)):
    if c[i]==int(c[i]):
        e.append(c[i])
for i in range(len(e)):
    sum+=(e[i]*e[i])
print(int(sum))