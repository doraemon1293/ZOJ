import sys

d=[1,1,1]


for n in sys.stdin.readlines():
    n=int(n.strip())
    if n==1 or n==2:
        print d[n]
    else:
        i=3
        while i<=n:
            d.append(d[i-2]+d[i-1])
            i+=1
        print d[n]
    
    