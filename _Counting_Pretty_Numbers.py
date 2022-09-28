n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=[]
    for i in range(a,b+1):
        if i>1:
            tmp=i
            if tmp%10==2 or tmp%10==3 or tmp%10==9:
                c.append(i)
    print(len(c))