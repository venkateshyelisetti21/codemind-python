a,b=map(int,input().split())
tmp=10**b
tmp1=10**(len(str(a))-b)
x=a%tmp
y=a//tmp1
print(abs(x-y))