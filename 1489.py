import sys
for n in sys.stdin.readlines():
    n=int(n.strip())
    if n%2 ==0 or n==1:
        print "2^? mod %d = 1" %n
    else:
        x=1
        product=2**x
        while product%n!=1:
            x+=1
            product=(product*2)%n
        print "2^%d mod %d = 1"%(x,n)
            