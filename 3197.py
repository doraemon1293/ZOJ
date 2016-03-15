import sys
        
#sys.stdin=open("test.txt","r")
testcases=int(sys.stdin.readline())
for testcase in range(testcases):
    n=int(sys.stdin.readline())
    a=[-1]*5001
    for i in range(1,n+1):
        x,y=map(int,sys.stdin.readline().strip().split())
        if a[x]<=y:
            a[x]=y

    for x in range(1,n+1):
        a[x]=max(a[x-1],a[x])
    #print a

    left=1
    ans=0
    
    while left<=n:
        left=a[left]+1
        ans+=1
    print ans
        
                
        
                
            
    