import math
n=int(input())
sq=math.sqrt(n)
c=0
for i in range(n):
    if sq==i:
        c=True
        break
if c==True:
    print(True)
else:
    print(False)