n=int(input())
n1=0
n2=1
c=0
if n<=0:
    print(n1)
elif n==1:
    print(n1)
else:
    while c<n:
        print(n1,end=' ')
        tmp=n1+n2
        n1=n2
        n2=tmp
        c+=1