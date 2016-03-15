import sys
from time import strptime

#sys.stdin=open("test.txt","r")
n=int( sys.stdin.readline() )
for i in range(n):
    s=sys.stdin.readline().strip().split()
    date1=strptime(' '.join(s[:3]), '%Y %m %d')
    date2=strptime(' '.join(s[3:6]), '%Y %m %d')
    if date1<date2:
        print "javaman"
    elif date1>date2:
        print "cpcs"
    else:
        print "same"
    