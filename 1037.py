import sys
lines=sys.stdin.readlines()
num=int(lines[0])
for i in range(1,num+1):
    n,m=[int(x) for x in lines[i].strip().split()]
    print "Scenario #%d:" %i
    if n%2==1 and m%2==1:
        print "%.2f" %(n*m+0.41)
    else:
        print "%.2f" %(n*m) 
    print
    