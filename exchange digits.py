from itertools import permutations
import sys

a,b=input().split()
if len(a)<len(b):
    print(-1)
    sys.exit()
b=int(b)
a=sorted(a)
m=permutations(a)
arr=[]
for i in m:
    arr.append(int(''.join(i)))
    
arr=list(set(arr))
arr.sort()
if arr[-1]<b:
    print(-1)
    sys.exit()
    
for j in arr:
    if j>b:
        print(j)
        sys.exit()
        
print(-1)
