import math
def a(x,y):
    c=[]
    for i in range(x,y+1):
        if i>1:
            for j in range(2,int(math.sqrt(i)) +1):
                if i%j==0:
                    break
            else:
                c.append(i)
    b=len(c)
    return b
x=int(input())
y=int(input())
print(a(x,y))