n=int(input())
n1=n%2
if n<9:
    c5=0
    if n1==0:
        c1=2
    else:
        c1=1
    c2=(n-c1)//2
    
else:
    c5=(n-4)//5
    n2=c5%2
    if n2==1 and n1==1:
        c1=2
    elif n2==1 and n1==0:
        c1=1
    elif n2==0 and n1==1:
        c1=1
    else:
        c1=2
    c2=(n-c1-(5*c5))//2
    
print(c1+c2+c5)
print(c1)
print(c2)
print(c5)