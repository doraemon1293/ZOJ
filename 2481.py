import sys
for line in sys.stdin.readlines()[:-1:]:
    ans=list( set( line.strip().split()[1:] ) )
    ans.sort()
    print ' '.join(ans)