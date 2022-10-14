n=int(input())
m=int(input())
a=m+n
b=m+n
while True:
    a+=1
    tmp=a
    for i in range(2,tmp//2 +1):
        if tmp%i==0:
            break
    else:
       print(a-b)
       break