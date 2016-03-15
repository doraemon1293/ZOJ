import sys
#sys.stdin=open("test.txt","r")
t=int(sys.stdin.readline())
for tt in xrange(t):
    s=sys.stdin.readline().strip()
    if s=="Faster":
        sys.stdin.readline()
        print min( map(int,sys.stdin.readline().strip().split()))
    elif s=="Higher":
        sys.stdin.readline()
        print max( map(int,sys.stdin.readline().strip().split()))
    elif s=="Stronger":
        sys.stdin.readline()
        print max( map(int,sys.stdin.readline().strip().split()))
        
        
        
        