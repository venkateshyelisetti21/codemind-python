n=int(input())
sq=n*n
sum=0
while sq:
    r=sq%10
    sum+=r
    sq//=10
if n==sum:
    print('Neon Number')
else:
    print('Not Neon Number')