a=list(map(float,input().split()))
n=len(a)
a.sort()
while n>=3:
    if a[n-1]< sum(a[:n-1]):
        m=n
        break
    else:
        m=0
        n-=1

print(m,end='')