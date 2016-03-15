import sys

sys.stdin=open("test.txt","r")
n=int( sys.stdin.readline() )
for i in range(n):
    s=map(int,sys.stdin.readline().strip().split())
    if s[0]-s[1]>s[0]-s[2]:
        print "B"
    else:
        print "A"