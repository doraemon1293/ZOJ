import sys
import math
nSet=int(sys.stdin.readline().strip())

for n in range(nSet):
    line=sys.stdin.readline().strip()
    x=float(line.split()[0])
    y=float(line.split()[1])
    radius=x*x+y*y
    r=0
    year=0
    while r<radius:
        r+=100/math.pi
        year+=1
    print "Property %d: This property will begin eroding in year %d." %(n+1,year)
    #Property 1: This property will begin eroding in year 1. 
print "END OF OUTPUT."