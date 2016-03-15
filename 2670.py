import sys
#sys.stdin=open("test.txt","r")

lines=map(int,sys.stdin.readlines())
for n in lines:
    for i in xrange(n-1):
        print ' '.join( ['0']*n )
    print ' '.join(['0']*(n-1)+['100'])
    print 
