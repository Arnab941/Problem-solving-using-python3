n=int(input())
t=n**2
moj=[[0 for i in range(n)] for j in range(n)]
star=0
end=n-1
m=1
a=[(0,0)]
while m<=t:
        for i in range(star,end+1):
            moj[star][i]=m
            if m%11==0:
                a.append((star,i))
            m+=1
        for i in range(star+1,end+1):
            moj[i][end]=m
            if m%11==0:
                a.append((i,end))
            m+=1
        for i in range(end-1,star-1,-1):
            moj[end][i]=m
            if m%11==0:
                a.append((end,i))
            m+=1
        for i in range(end-1,star,-1):
            moj[i][star]=m
            if m%11==0:
                a.append((i,star))
            m+=1
        
        star+=1
        end-=1
    
for i in moj:
        print(*i,sep=' ')
        
print('No of power points :',len(a))
for i in a:
    print(i)