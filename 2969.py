import sys
sys.stdin=open("test.txt","r")
t=int(sys.stdin.readline())
for tt in xrange(t):
    n=int(sys.stdin.readline())
    a=map( int ,sys.stdin.readline().strip().split() )[::-1]
    #print a
    b=[]
    for i,c in enumerate(a):
        b.append(i*c)
    if b==[0]:
        print 0
    else:
        print ' '.join(map(str,b[::-1])[:-1:])
    
        
    
    
    