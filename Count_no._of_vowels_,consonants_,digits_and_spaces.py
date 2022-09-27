n=input()
n=n.lower()
a=['a','e','i','o','u']
b=['0','1','2','3','4','5','6','7','8','9']
v=0
d=0
s=0
for i in n:
    if i==' ':
        s+=1
    elif i in b:
        d+=1
    elif i in a:
        v+=1
c=len(n)-(v+d+s)
print('Vowels:',v)
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',s)
    