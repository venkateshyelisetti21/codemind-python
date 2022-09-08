n=int(input())
a=list(map(int,input().split()))
x=sum(a)//n
if x in a:
    print(True)
else:
    print(False)