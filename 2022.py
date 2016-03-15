import sys
for n in sys.stdin.readlines()[1::]:
    n=int(n.strip())
    ans=0
    while n/5:
        ans+=n/5
        n/=5
    print ans