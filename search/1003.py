import sys
flag1=0
flag2=0
def dfs(x,y,n):
    global flag1, flag2
    if y==1:
        flag2=1
        if x==1:
            flag1=1
    if (n>100 or flag1==1 and flag2==1):
        return
    if (y%n==0):
        dfs(x,y/n,n+1)
    if (x%n==0):
        dfs(x/n,y,n+1)
    dfs(x,y,n+1)
for line in sys.stdin.readlines():
    a,b=line.strip().split(' ')
    a=int(a)
    b=int(b)
    if a<b: 
        temp=a
        a=b
        b=temp
    flag1=0
    flag2=0
    dfs(a,b,2)
    if (flag2==1 and flag1==0):
        print b
    else:
        print a
    