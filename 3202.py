import sys
#sys.stdin=open("test.txt","r")
t=int( sys.stdin.readline() )
for tt in range(t):
    n=int( sys.stdin.readline() )
    bids=map(int,sys.stdin.readline().strip().split())
    max=-1
    max0=-2
    for i,bid in enumerate(bids):
        if bid>max:
            winner=i
            max0=max
            max=bid
        else:
            if bid>max0:
                max0=bid
    print (winner+1),max0
            
    