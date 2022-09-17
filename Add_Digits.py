n=int(input())
sum=0
while n>0:
    r=n%10
    sum+=r
    n=n//10
    if n==0 and sum>9:
        n=sum
        sum=0
print(sum)