n=int(input())
a=[]
for i in range(n):
    a.append(i+1)
holes=list(map(int,input().split()))
b=int(input())
balls=list(map(int,input().split()))
for j in balls:
    y=0
    for k in range(n-1,-1,-1):
        if j<=holes[k]:
            y=1
            print(k+1,end=' ')
            a[k]-=1
            if a[k]==0:
                holes[k]=-1
            break
    if y==0:
        print(0,end=' ')