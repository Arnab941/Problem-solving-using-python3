n=int(input())
a=[]
for i in range(n):
    m=int(input())
    a.append(m)

t=int(input())    
v=[[[-1 for i in  range(4)] for i1 in range(n+1)]for i3 in range(t+1)]
def sheldon(t,n,k):
    if t==0 and k==0:
        v[t][n][k]=True
        return v[t][n][k]
    elif t==0 and k!=0:
        v[t][n][k]=False
        return v[t][n][k]
    elif n==0:
        v[t][n][k]=False
        return v[t][n][k]
    if a[n-1]<=t:
        v[t][n][k]=((sheldon(t-a[n-1],n-1,k-1)) or (sheldon(t,n-1,k)))
    else:
        v[t][n][k]=sheldon(t,n-1,k)
        
    return v[t][n][k]
                
j=sheldon(t,n,3)
print(j)