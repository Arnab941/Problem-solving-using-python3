m,p,r=map(float,input().split())
if r==0:
    c=m*p
else:
    x=1/(1+(r/1200))
    c=m*x*(1-(x**(p)))/(1-x)
    c=float('{:.11f}'.format(c))
print(round(c)) 