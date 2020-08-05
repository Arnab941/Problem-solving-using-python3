look_up = [[0 for i in range(1502)] for j in range(1502)]
def lu(i,j):
    i,j=max(i,j),min(i,j)
    if look_up[i][j]==0:
        if i==j:
            look_up[i][j]=1
        else:
            look_up[i][j]=1+lu(i-j,j)
            
    return look_up[i][j]
        

#taking input
min_len=5
max_len=7
min_wid=3
max_wid=4
count=0
for i in range(min_len,(max_len+1)):
    for j in range(min_wid,(max_wid+1)):
        k=lu(i,j)
        count+=k
        
print(count)