import math
t=int(input())
for i in range(t):
    n=int(input())
    pattern=list(map(int,input().split()))
    ans=1
    for j in range(n):
        m=0
        start_pos=j
        p=-1
        while p!=0:
            start_pos=pattern[start_pos]-1
            m+=1
            if start_pos==j:
                p=0
        ans=(ans*m)//math.gcd(ans,m)
    print(ans) 