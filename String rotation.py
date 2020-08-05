import sys
s=input()
ls=len(s)
n=int(input())
m=''
start_loc=0
for i in range(n):
    direc,loc=map(str,input().split())
    loc=int(loc)
    if direc=='L':
        start_loc=(start_loc+loc)%ls
        m+=s[start_loc]
    else:
        start_loc=(start_loc-loc)%ls
        m+=s[start_loc]
        
if n>ls:
    print('NO',end='')
    sys.exit()

else:
    for i in range(ls-n+1):
        s1=s[i:(i+n)]
        print(s1)
        s2=sorted(s1)
        m1=sorted(m)
        if m1==s2:
            print('YES',end='')
            sys.exit()
    
    print('NO',end='')