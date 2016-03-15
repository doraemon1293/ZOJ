import sys
#sys.stdin=open('test.txt','r')
lines=sys.stdin.readlines()[:-1]
pi=3.1415926535
for line in lines:
    d,v=map(int,line.strip().split())
    print "%.3f" %(d**3-6*v/pi)**(1.0/3)