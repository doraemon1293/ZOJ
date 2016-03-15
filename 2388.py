import sys
for line in sys.stdin.readlines()[1::]:
    sum,d=[int(x) for x in line.strip().split()]
    a=(sum+d)/2.0
    b=(sum-d)/2.0
    if a==int(a) and b==int(b)and a>=0 and b>=0:
        print int(a),int(b)
    else:
        print "impossible"