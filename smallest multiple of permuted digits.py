from itertools import permutations
import sys
n=sorted(input())
d=int(input())
m=permutations(n)
a=[]
for i in m:
    b=int(''.join(i))
    if b not in a:
        if b%d==0:
            print(b)
            sys.exit()
        a.append(b)
        
print(-1)