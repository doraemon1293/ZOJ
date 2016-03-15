import sys
for line in sys.stdin.readlines()[1:]:
    print '.'.join([str( int(line.strip()[i:i+8],2) ) for i in range(0,32,8)])
    
    