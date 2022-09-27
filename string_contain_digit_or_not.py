n=input()
c=0
a=['1','2','3','4','5','6','7','8','9','0']
for i in n:
    if i in a:
        c+=1
if c:
    print('Contains',c,'digit')
else:print("Doesn't contain digit" )