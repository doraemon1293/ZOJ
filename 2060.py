import sys
a=[0]*1000000
a[0]=7%3
a[1]=11%3
for i in range(2,1000000):
    a[i]=(a[i-1]+a[i-2])%3

for line in sys.stdin.readlines():
    if a[ int(line.strip()) ]%3:
        print "no"
    else:
        print "yes"
    