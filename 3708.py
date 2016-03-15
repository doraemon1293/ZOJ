import sys
sys.stdin=open('test.txt','r')
t=int(sys.stdin.readline())

    
for tt in range(t):
    n,m=map(int,sys.stdin.readline().strip().split())
    start=map(int,sys.stdin.readline().strip().split())
    end=map(int,sys.stdin.readline().strip().split())
    temp=zip(start,end)
    tran=set( [(x,y) if x<y else(y,x) for x,y in temp] )
    print "%.3F" % (float( len(tran) )/n)