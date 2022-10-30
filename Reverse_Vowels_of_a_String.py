n=input()
tmp=''
x='aeiouAEIOU'
for i in n:
    if i in x:
        tmp+=i
tmp1=''
for j in n:
    if j in x:
        tmp1+=tmp[-1]
        tmp=tmp[:-1]
    else:
        tmp1+=j
print(tmp1)