import sys
for line in sys.stdin.readlines()[1::]:
    print line.strip().split()[1]+" will survive"