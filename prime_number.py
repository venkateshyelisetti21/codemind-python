n=int(input())
c=0
for i in range(2,n):
    if n%i==0:
        break
else:
    c=True
if c==True:
    print('prime')
else:
    print('not a prime')