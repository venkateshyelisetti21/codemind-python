n=input()
n=n.split()
tmp=0
tmp1=0
a=[]
b=[]
for i in n:
    tmp=i
    break
for i in n:tmp1=i
for i in tmp:a.append(i)
for i in tmp1:b.append(i)
print(min(a),max(b))