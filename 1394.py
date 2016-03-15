import sys
import math
#sys.stdin=open('test.txt','r')
pi=3.14159
for line in sys.stdin.readlines()[1:-1:3]:
    r,y,angle=map(int,line.strip().split())
    if angle>180:
        angle=360-angle
    dis=2*pi*r*angle/360*2
    #print dis
    if dis<=y*5:
        print "YES %d" % int(math.floor(y-dis/5))
    else:
        print "NO %d" %int(y*5)