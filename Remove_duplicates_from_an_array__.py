n=int(input())
a=list(map(int,input().split()))
res=list(set(a))
for i in range(len(res)):
    print(res[i],end=' ')
    