def prime(n):
    if n==1:
        return False
    for i in range(2, n // 2 + 1):
        if n%i == 0:
            return False
    return True
    
n = int(input())
found = 0
for i in range(2, n // 2 + 1):
    if n%i == 0:
        if prime(i) and prime(n // i):
            print(i, n // i)
            found = 1
            break
if found == 0:
    print(-1)