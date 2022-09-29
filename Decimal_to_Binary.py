t=int(input())
for i in range(t):
    def bin(n):
        if n > 1:
            bin(n//2)
        print(n % 2,end = '')
    n=int(input())
    bin(n)
    print()