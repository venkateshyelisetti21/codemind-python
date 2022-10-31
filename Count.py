n=int(input())
a=list(map(int,input().split()))
b=c=0
for i in a:
    if i%2==0:
        b+=1
    else:c+=1
print(b,c)