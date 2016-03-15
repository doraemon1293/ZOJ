import sys

blocks=int(sys.stdin.readline().strip())

for block in range(blocks):
    sys.stdin.readline()
    lines=int(sys.stdin.readline().strip())
    for line in range(lines):
        s=[x[::-1] for x in sys.stdin.readline().strip().split(' ')]
        
        ans=" ".join(s)

        print ans
    if block!=blocks-1: print
    

        
    
