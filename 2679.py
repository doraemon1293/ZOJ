import sys
#sys.stdin=open("test.txt","r")
n=int(sys.stdin.readline())
for nn in xrange(n):
    turkeys=int(sys.stdin.readline())
    x,y,z=map(int,sys.stdin.readline().strip().split())
    sum=x*1000+y*100+z*10
    f=0
    for a1 in xrange(9,0,-1):
        if f==1:
            break
        for a5 in xrange(9,-1,-1):
            if (sum+(a1*10000)+a5)% turkeys==0:
                print a1,a5,(sum+a1*10000+a5)/turkeys
                f=1
                break
    if f==0:
        print 0
        
            
    