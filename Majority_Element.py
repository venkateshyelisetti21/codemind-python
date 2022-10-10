n=int(input())
l1=list(map(int,input().split()))
l=[(l1.count(x),x) for x in set(l1)]
a=max(l)[0]
for i in l:
   if i[0]==a:
       print(i[1])