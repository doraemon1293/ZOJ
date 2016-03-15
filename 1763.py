import sys
line = [float(x.strip()) for x in sys.stdin.readlines()]

for n in range(1,len(line)-1):
    print "%.2f" %(line[n]-line[n-1])
print "End of Output"

                                                        
    