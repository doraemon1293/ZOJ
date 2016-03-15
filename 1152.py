import sys
blocks=int(sys.stdin.readline().strip())
for block in range(blocks):
    l=0
    sys.stdin.readline()
    n,m=sys.stdin.readline().strip().split(' ')
    n=int(n)
    m=int(m)
    while n!=0 or m!=0:
        l+=1
        ans=0
        for a in range(1,n):
            for b in range(a+1,n):
                if (a*a+b*b+m) % (a*b) ==0:
                    ans+=1
        print "Case %d:%d" %(l,ans)
        n,m=sys.stdin.readline().strip().split(' ')
        n=int(n)
        m=int(m) 
    if block!=blocks-1:print     