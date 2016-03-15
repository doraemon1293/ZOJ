import sys

def do(ca,canow,cb,cbnow,n):
    if cbnow==n:
        return
    else:
        if cbnow>ca:
            print "pour B A"
            if (cbnow-(ca-canow)==n):
                return
            print "empty A"
            do(ca,0,cb,cbnow-(ca-canow),n)
        else:
            print "pour B A"
            print "fill B"
            do(ca,cbnow,cb,cb,n)
for line in sys.stdin.readlines():
    ca,cb,n=[int(x) for x in line.strip().split()]
    print "fill B"
    do(ca,0,cb,cb,n)
    print ("success")
        