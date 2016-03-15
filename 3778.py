import sys
import math
t=int(sys.stdin.readline())
    
for tt in range(t):
    n,m=map(int,sys.stdin.readline().strip().split())
    a=map(int,sys.stdin.readline().strip().split())
    ans=int( math.ceil( float(sum(a))/m ) )
    if ans>=max(a):
        print ans
    else:
        print max(a