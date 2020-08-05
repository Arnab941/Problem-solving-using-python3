n=list(input())
c=0
n1=0
a=[]
star=[]
t1=0
for i in n:
    if i=='(' or i=='{' or i=='[':
        a.append(i)
        star.append(0)
        n1+=1
    elif i=='*':
        for j in range(n1-1,-1,-1):
            if star[j]==2:
                break
            else:
                star[j]+=1 
    elif i==')':
        if n1==0:
            t1=-1
        m=''
        while n1>0 :
            m=a.pop()
            n2=star.pop()
            n1-=1
            if m=='(':
                if n2!=2:
                    t1=-1
                else:
                    c+=1
                    break
            else:
                t1=-1
    elif i=='}':
        m=''
        if n1==0:
            t1=-1
        while n1>0 :
            m=a.pop()
            n2=star.pop()
            n1-=1
            if m=='{':
                if n2!=2:
                    t1=-1
                else:
                    c+=1
                    break
            else:
                t1=-1
    elif i==']':
        m=''
        if n1==0:
            t1=-1
        while n1>0 :
            m=a.pop()
            n2=star.pop()
            n1-=1
            if m=='[':
                if n2!=2:
                    t1=-1
                else:
                    c+=1
                    break
            else:
                t1=-1
if t1==0:
    print('Yes',end=' ')
else:
    print('No',end=' ')
print(c)