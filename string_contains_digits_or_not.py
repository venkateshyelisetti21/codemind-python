n=int(input())
for i in range(n):
    a=0
    b=input()
    for j in range(len(b)):
        if ord(b[j])>=48 and ord(b[j])<=57:
            a+=1
            break
    if a:
        print('Yes',end='
')
        
    else:
        print('No',end='
')
        