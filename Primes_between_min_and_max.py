n=int(input())
m=list(map(int,input().split()))
d=0
k=max(m)
l=min(m)
f=False
g=False
for i in range(len(m)):
    if f==False and (m[i]==k or m[i]==l):
        f=True
        g=True
        a=i
    if g==False or m[i]<=1:
        continue
    for j in range(2,int(m[i]**0.5)+1):
        if m[i]%j==0:
            break
    else:
        d+=1
    if f==True and (m[i]==k or m[i]==l) and i!=a:
        break
print(d)