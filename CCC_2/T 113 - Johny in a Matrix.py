n=int(input())
l=list()
r=0             
c=0
mn=0
for i in range(n):
    v=list(map(int,input().split()))
    l.append(v)
for i in range(n):
    for j in range(n-1):
        r=r+l[i][j]*l[i][j+1]
for i in range(n-1):
    r=r+l[i][-1]*l[i+1][0] 
for i in range(n):
    for j in range(n-1):
        c=c+l[j][i]*l[j+1][i]
for i in range(n-1):
    c=c+l[n-1][i]*l[0][i+1]
if(c<r):
    print('column-major')
else:
    print('row-major')