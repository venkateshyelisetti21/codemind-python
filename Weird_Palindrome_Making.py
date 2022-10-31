t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=0
    for i in a:
        if i%2 !=0:
            b+=1
    print(b//2)