n=int(input())
tmp=n
a=0
while True:
    for i in range(2,tmp//2 +1):
        if tmp%i==0:
            break
    else:
        a=tmp
        break
    tmp+=1
tmp1=n
b=0
while True:
    for i in range(2,tmp1//2 +1):
        if tmp1%i==0:
            break
    else:
        b=tmp1
        break
    tmp1-=1
x=abs(n-a)
y=abs(n-b)
print(min(x,y))