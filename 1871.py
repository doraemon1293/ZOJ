import sys
for line in sys.stdin.readlines():
    d=abs( int(line.strip().split()[0])-int(line.strip().split()[1]) )
    n=int(d**(0.5))
    if d:
        if n**2==d:
            print 2*n-1
        elif d-n**2>n:
            print 2*n+1
        else:
            print 2*n
    else:
        print 0