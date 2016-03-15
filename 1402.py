import sys
for line in sys.stdin.readlines()[:-1:]:
    line=[int(x) for x in line.strip().split()]
    n=line[0]
    req=line[1::]
    t=0
    for i in range(n):
        if sum(req[0:i])==sum(req[i::]):
            print "Sam stops at position %d and Ella stops at position %d." %(i,i+1)
            t=1
            break
    if t==0: print "No equal partitioning."

            
        