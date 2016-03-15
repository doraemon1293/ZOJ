import sys
for line in sys.stdin.readlines()[1::]:
    a=[float(x) for x in line.strip().split()[1::]]
    ave=sum(a)/len(a)
    ans=0.0
    for x in a:
        if x >ave:ans+=1
    print "%.3f%%" %(ans/len(a)*100)
        
    