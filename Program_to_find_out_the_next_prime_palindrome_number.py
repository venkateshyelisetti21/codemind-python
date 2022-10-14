n=int(input())
while True:
    n+=1
    tmp=n
    rev=int(str(tmp)[::-1])
    if tmp==rev:
        for i in range(2,tmp//2 +1):
            if tmp%i==0:
                break
        else:
            print(tmp)
            break
    else:
        continue