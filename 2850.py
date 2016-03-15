import sys
#sys.stdin=open("test.txt","r")
n,m= map(int,sys.stdin.readline().strip().split())
while n!=0 or m!=0:
    a=[]
    for i in xrange(n):
        a.append(map(int,sys.stdin.readline().strip().split()))
    ans=1#Yes
    flag=0#all covered
    for i in xrange(n):
        for j in xrange(m):
            if a[i][j]==0:
                flag=1
                if i-1>=0 and a[i-1][j]==0:
                    ans=0
                    break
                if i+1<n and a[i+1][j]==0:
                    ans=0
                    break
                if j-1>=0 and a[i][j-1]==0:
                    ans=0
                    break
                if j+1<m and a[i][j+1]==0:
                    ans=0
                    break
    if ans and flag:
        print "Yes"
    else:
        print "No"
    n,m= map(int,sys.stdin.readline().strip().split())
