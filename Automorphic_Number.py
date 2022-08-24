n=int(input())
sq=n*n
l=len(str(n))
res=sq%(10**l)
if n==res:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')