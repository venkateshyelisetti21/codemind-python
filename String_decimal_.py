t=int(input())
for i in range(t):
    a=input()
    b=['0','1','2','3','4','5','6','7','8','9']
    tmp=0
    for i in a:
        if i not in b:
            tmp+=1
    if tmp:print(False)
    else:print(True)