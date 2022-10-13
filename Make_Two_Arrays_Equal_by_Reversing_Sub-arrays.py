n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
a.sort()
b.sort()
cnt=0
if m==n:
    for i in a:
        if i in b:
            cnt+=1
    if cnt==n:print(True)
    else:print(False)
else:print(False)