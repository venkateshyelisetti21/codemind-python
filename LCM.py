a,b=map(int,input().split())
if a>b:tmp=a
else:tmp=b
lcm=0
while True:
    if tmp%a==0 and  tmp%b==0:
        lcm=tmp
        break
    tmp+=1
print(lcm)