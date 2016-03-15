import sys
lines = [x.strip() for x in sys.stdin.readlines()]
for s in lines[1::]:
    print s[::-1]
    
 