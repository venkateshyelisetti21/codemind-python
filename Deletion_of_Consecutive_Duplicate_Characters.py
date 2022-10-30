n=int(input())
for i in range(n):
    a=list(input())
    tmp=0
    for j in range(len(a)-1):
        if a[j]==a[j+1]:
            tmp+=1
    print(tmp)
    