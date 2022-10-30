n=input()
a='0123456789'
b=0
for i in n:
    if i in a:
        b+=int(i)
print(b)