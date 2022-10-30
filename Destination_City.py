n=int(input())
for i in range(n):
    a=list(input().split(' '))
print(*a[-1],sep='')