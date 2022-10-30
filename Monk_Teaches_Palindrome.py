n=int(input())
for i in range(n):
    a=input()
    b=a[::-1]
    if a==b:
        print('YES',end=' ')
        if len(a)%2==0:
            print('EVEN')
        else:
            print('ODD')
    else:
        print('NO')