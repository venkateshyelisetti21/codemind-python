a=input()
a.split()
b=0
c=0
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        c+=1
    else:
        c=0
    if(b<c):
        b=c
print(b+1)