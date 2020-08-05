look_up=[-1]*10000001
look_up[1]=0
look_up[2]=1
def mosti(n):
    if look_up[n]==-1:
        for i in range(3,n+1):
            look_up[i]=(((i-1)*look_up[i-1])%1000000007)+(((i-1)*look_up[i-2])%1000000007)
    
    return look_up[n]
n=int(input())
print(mosti(n)%1000000007,end='')