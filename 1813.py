import sys
pi=3.1415927
for n,line in enumerate(sys.stdin.readlines()):
    d=float(line.strip().split()[0])
    r=int(line.strip().split()[1])
    t=float(line.strip().split()[2])
    if r==0:break
    print "Trip #%d: %.2f %.2f" %(n+1, pi*d*r/5280/12,pi*d*r/5280/12/t*3600 )
    