m=int(input())
n=int(input())
a=[]
for i in range(m,n+1):
    c=0
    if i:
        tmp=i
        while tmp:
            r=tmp%10
            if r:
                if i%r==0:
                    c+=1
            tmp//=10
    if len(str(i))==c:
        a.append(i)
print(*a)