n=int(input())
sq=n*n
rev=int(str(n)[::-1])
sq1=rev*rev
rev1=int(str(sq1)[::-1])
if sq==rev1:
    print(True)
else:
    print(False)