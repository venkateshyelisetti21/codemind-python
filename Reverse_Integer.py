n=int(input())
if n>=0:
    rev=str(n)[::-1]
    rev=int(rev)
    print(rev)
else:
    n=abs(n)
    rev=str(n)[::-1]
    rev=int(rev)
    tmp='-'+str(rev)
    print(tmp)