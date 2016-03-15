import sys
from math import log10
#sys.stdin=open('test.txt','r')
testcases=int(sys.stdin.readline())

for testcase in range(testcases):
    ka,acid,m,n=(1,1,1,1)
    while ka+acid+m+n!=0:
        line=sys.stdin.readline().strip()
        if line:
            ka,acid,m,n=map(float,line.split())
            if ka+acid+m+n!=0:
                ph=-1*log10(
                            ( (4*m*n*ka*acid+ka*ka)**0.5-ka )/(2*n)
                            
                            )
                print "%.3f" %ph
    if testcase!=testcases-1:
        print
        
        
        