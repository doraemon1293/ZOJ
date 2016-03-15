import sys

def dfs(x,y,s):
    #global a
    if s==target:
        return True
    a[x][y]='S'
    if y-1>=0 and a[x][y-1]=='.':
        if dfs(x,y-1,s+1):
            return True
    if y+1<m and a[x][y+1]=='.':
        if dfs(x,y+1,s+1):
            return True
    if x-1>=0 and a[x-1][y]=='.':
        if dfs(x-1,y,s+1):
            return True
    if x+1<n and a[x+1][y]=='.':
        if dfs(x+1,y,s+1):
            return True
    a[x][y]='.'
    return False            

#sys.stdin=open("test.txt","r")
n,m=[int(x) for x in sys.stdin.readline().strip().split()]
while n!=0 or m!=0:
    a=[]
    for i in range(n):
        a.append(list(sys.stdin.readline().strip()))
    target=sum([x.count('.') for x in a])
    
    if a[0][0]=='S':
        print "No"
    elif dfs(0,0,1):
            print "YES"
    else:
        print "NO"
    n,m=[int(x) for x in sys.stdin.readline().strip().split()]

    
         