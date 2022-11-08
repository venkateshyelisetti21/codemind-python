n=int(input())
a=1
for i in range(1,n+1):
    for j in range(a,n+1):
        print(str(j),end=' ')
    print()
    a+=1
    