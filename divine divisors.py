n=int(input())
m=int(n**(1/2))
a=['1']
b=[str(n)]
for i in range(2,m+1):
    if n%i==0:
        a.append(str(i))
        if (n/i)!=m:
            b.append(str(n//i))
            
b=b[::-1]
a1=' '.join(a)
b1=' '.join(b)
print(a1+' '+b1)