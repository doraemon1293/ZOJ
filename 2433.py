import sys
sys.stdin=open('test.txt','r')
testcases=int(sys.stdin.readline())
    
for testcase in range(testcases):
    sys.stdin.readline()
    n=int(sys.stdin.readline().strip())
    a=map(int,sys.stdin.readline().strip().split())
    a=[0]+a
    if n<4:
        print 0
    else:
        mini=sys.maxint
        for i in range(2,n-1):
            if a[i]-a[i-1]<mini:
                mini=a[i]-a[i-1]
                city=i
        print a[-1]+mini
        print city+1,1,n,city
    if testcase!=testcases-1:
        print

        