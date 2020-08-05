import sys
h,j=map(int,input().split(','))
if j==1:
    print(h)
    sys.exit()
j-=1
h1=int(h**(1/2))+1
a=[1]
u=1
for i in range(2,h1):
    if h%i==0:
        u+=1
        j-=1
        a.append(i)
        n=h//i
        if j==0:
            print(n)
            sys.exit()
        if i==n:
            a=a[:-1]
if j>u:
    print(1)
    sys.exit()
else:
    a=a[::-1]
    print(a[j-1])  