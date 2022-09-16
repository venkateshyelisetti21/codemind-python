n=int(input())
a=list(map(int,input().split()))
sum=0
for i in a:
    sum+=i
avg=sum//n
c=0
for i in a:
    if i>=avg:
       c+=1
print(c)