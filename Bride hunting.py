n,m=map(int,input().split())
a=[]
for i in range(n):
    j=list(map(int,input().split()))
    a.append(j)
a[0][0]=0
    
def count(i,j):
    m1=0
    if (j-1)>=0 and a[i][j-1]==1:
        m1+=1
    if (j+1)<m and a[i][j+1]==1:
        m1+=1
    if (i-1)>=0 and a[i-1][j]==1:
        m1+=1
    if (i+1)<n and a[i+1][j]==1:
        m1+=1
    if (i-1)>=0 and (j+1)<m and a[i-1][j+1]==1:
        m1+=1
    if (i+1)<n and (j+1)<m and a[i+1][j+1]==1:
        m1+=1
    if (i+1)<n and (j-1)>=0 and a[i+1][j-1]==1:
        m1+=1
    if (i-1)>=0 and (j-1)>=0 and a[i-1][j-1]==1:
        m1+=1
    return m1

quality=[0]
dist=[]
loc=[]
for i in  range(n):
    for j in range(m):
        if a[i][j]==1:
            t=count(i,j)
            if t>0:
                if t>quality[0]:
                    quality=[]
                    quality.append(t)
                    dist=[]
                    dist.append(max(i,j))
                    loc=[]
                    loc.append((i+1,j+1))
                elif t==quality[0]:
                    quality.append(t)
                    dist.append(max(i,j)-1)
                    loc.append((i+1,j+1))               

if len(quality)==1:
    if quality[0]==0:
        print('No suitable girl found')
    else:
        print(str(loc[0][0])+':'+str(loc[0][1])+':'+str(quality[0]))
else:
    if len(list(set(dist)))==1:
        print('Polygamy not allowed')
    else:
        f=dist.index(min(dist))
        print(str(loc[f][0])+':'+str(loc[f][1])+':'+str(quality[0]))
        
        