import math

x1,y1=map(float,input().split())
x2,y2=map(float,input().split())
x3,y3=map(float,input().split())
a=(((x1-x2)**2)+((y1-y2)**2))**(1/2)
a=round(a,11)
b=(((x2-x3)**2)+((y2-y3)**2))**(1/2)
b=round(b,11)
c=(((x1-x3)**2)+((y1-y3)**2))**(1/2)
c=round(c,11)
if a==0 or b==0 or c==0:
    print('Not Possible',end='')
else:
    s=(a+b+c)/2
    s=round(s,11)
    g=(s*(s-a)*(s-b)*(s-c))**(1/2)
    g=round(g,11)
    R=(a*b*c)/(4*g)
    R=round(R,11)
    r=g/s
    r=round(r,11)
    ans=math.pi*((R+r)*(R-r))
    ans=round(ans,11)
    
    print('{:.2f}'.format(ans),end='')
    