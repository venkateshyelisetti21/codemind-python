p,r,t=map(int,input().split())
ci=p*(1+(r/100))**t
res="{:.2f}".format(ci)
print(res)
