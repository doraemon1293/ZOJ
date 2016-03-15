import sys

minx=sys.maxint
miny=sys.maxint
maxx=0
maxy=0
for line in sys.stdin.readlines()[:-1:]:
    x,y=[int(x) for x in line.strip().split()]

    if x==0 and y==0:
        print minx,miny,maxx,maxy
        minx=sys.maxint
        miny=sys.maxint
        maxx=0
        maxy=0
    else:
        if x<minx:
            minx=x
        if x>maxx:
            maxx=x
        if y<miny:
            miny=y
        if y>maxy:
            maxy=y
        