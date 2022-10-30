a=input()
b='0'
v='aeiouAEIOU'
for i in a:
    if i in v:
        if b[-1]!='V':
            b+='V'
    else:
        if b[-1]!='C':
            b+='C'
b=list(b)
b.remove(b[0])
print(''.join(b))