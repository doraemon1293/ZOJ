import sys
from math import log10,trunc
for line in sys.stdin.readlines()[1::]:
    n=int(line.strip())
    i=2
    sum=1
    while i<=n:
        sum+=log10(i)
        i+=1
    print trunc(sum)
        