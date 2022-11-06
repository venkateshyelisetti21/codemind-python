n=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    if i==l.count(i) and i not in b:
        b.append(i)
if len(b)!=0:
    print(*b)
else: 
    print('-1')