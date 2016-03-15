import sys
for line in sys.stdin.readlines()[:-1:]:
    n=int(line)
    i=1
    while n%2==0:
        n/=2
        i*=2
    print i