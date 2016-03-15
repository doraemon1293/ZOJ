import sys

for line in sys.stdin.readlines()[:-1:]:
    a=[int(x) for x in line.strip().split()]
    a[0]=0
    print sum( [(a[i+1]-a[i])*6+5 if a[i+1]>=a[i] else (a[i]-a[i+1])*4+5 for i in range(len(a)-1)])
    
    