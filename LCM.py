a,b=map(int,input().split())
lcm=0
if a>b:tmp=a
else:tmp=b
while True:
    if tmp%a==0 and tmp%b==0:
        lcm=tmp
        break
    tmp+=1
print(lcm)
    