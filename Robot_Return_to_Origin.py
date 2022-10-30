a=0
n=input()
for i in n:
    if i=='R' or i=='U':
        a+=1
    else:
        a-=1
if a:print(False)
else:print(True)