def is_prime(n):
    m=int(n**(1/2))
    c=0
    for i in range(3,(m+2),2):
        if n%i==0:
            c=1
            break
    if c==1:
        return 0
    else:
        return 1

n=int(input())
count=0
if n%2==0:
    n=n//2
    count+=1
    
i=3
while i<=n:
    if n%i==0:
        n=n//i
        if is_prime(i):
            count+=1
    i+=2     
    
print((2**(count))-1)