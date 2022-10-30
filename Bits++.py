n=int(input())
tmp=0
for i in range(n):
    x=input()
    if '++' in x:
        tmp+=1
    elif '--' in x:
        tmp-=1
print(tmp)