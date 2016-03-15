import sys
def do(p):
    mind=sys.maxint
    n=0
    for i in range(16):
        d=0
        for j in range(3):
            d+=(points[i][j]-p[j])**2
        if d<mind:
            mind=d
            n=i
    return n
    
    
lines=sys.stdin.readlines()
points=[]
for line in range(16):
    points.append([int(x) for x in lines[line].strip().split()])
#print points
for line in range(16,len(lines)):
    #print line
    p=[int(x) for x in lines[line].strip().split()]
    #print p
    if (-1 in p):
        break
    else:
        n=do(p)
        print "(%d,%d,%d) maps to (%d,%d,%d)" %(p[0],p[1],p[2],points[n][0],points[n][1],points[n][2])
            
    
    
    