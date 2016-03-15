import sys
for line in sys.stdin.readlines()[1::]:
    print str( int(line.strip().split()[0][::-1])+int(line.strip().split()[1][::-1]) )[::-1].lstrip('0')