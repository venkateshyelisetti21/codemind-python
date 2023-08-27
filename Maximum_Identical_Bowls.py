n=int(input())
arr=list(map(int,input().split()))
s=sum(arr)
while n:
    if s%n==0:
        print(n)
        break
    else:n-=1
    