n=int(input())
if n>=0:
    print(int(str(n)[::-1]))
else:
    rev=str(abs(n))[::-1]
    rev=int(rev)
    tmp='-'+str(rev)
    print(tmp)