import sys
#sys.stdin=open("test.txt","r")
t=int(sys.stdin.readline())
for tt in xrange(t):
    sys.stdin.readline()
    s1=map(lambda x:x[0],sys.stdin.readline().strip().split())
    sys.stdin.readline()
    s2=map(lambda x:x[0],sys.stdin.readline().strip().split())
    if s1==s2:
        print "SAME"
    else:
        print "DIFFERENT"
    
    