t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    a=[]
    b=[]
    c=[]
    for i in s:
        if i not in a:a.append(i)
        else:b.append(i)
    for i in a:
        if i not in b:
            c.append(i)
    if len(c):
        for i in c:
            print(i)
            break
    else:print(-1)