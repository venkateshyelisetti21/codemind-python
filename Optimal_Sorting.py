a=int(input())
for i in range(a):
    b=int(input())
    c=list(map(int,input().split()))
    d=sorted(c)
    if c==d:print(0)
    else:print(d[-1]-d[0])
    