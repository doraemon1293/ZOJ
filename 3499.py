import sys
#sys.stdin=open("test.txt","r")
testcases=int(sys.stdin.readline())

for testcase in range(testcases):
    n=int(sys.stdin.readline())
    a=map(float,sys.stdin.readline().strip().split())
    a.sort()
    if n&1:
        print "%.3f"%a[n/2]
    else:
        print "%.3f"%(( a[n/2-1]+a[n/2] ) /2)
    