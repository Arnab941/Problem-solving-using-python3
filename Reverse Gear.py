class Much:
    def chapless(self,d,t):
        print(d*t)
    def less(self,f,b,d,t):
        c=(b*t)+(((d-b)//(b-f))*t*(f+b))
        print(c)
    def chap(self,f,b,d,t):
        c1=((d-b)//(b-f))+1
        c2=d-(c1*(b-f))
        c=((c1*(b+f))+c2)*t
        print(c)


n=int(input())
for i in range(n):
    f,b,t,d=map(int,input().split())
    if b>=d:
        m=Much()
        m.chapless(d,t)
        
    elif (d-b)%(b-f)==0:
        m=Much()
        m.less(f,b,d,t)
        
    else:
        m=Much()
        m.chap(f,b,d,t)