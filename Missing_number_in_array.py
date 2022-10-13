n=int(input())
for i in range(n):
    x=int(input())
    b=list(map(int,input().split()))
    a=[]
    for i in range(1,x+1):
        a.append(i)
    c=[]
    for i in a:
        if i not in b:
           c.append(i) 
    for i in c:
        print(i)
        break