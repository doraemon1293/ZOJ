import sys
print '\n'.join(str(x) for x in [ len ( set( [x for x in line.strip().split() if line.strip().split().count(x)>1] ) ) for line in sys.stdin.readlines()[1::2]])            
