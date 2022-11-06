n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i not in a:
        a.append(i)
        print(i,l.count(i),end=' ')