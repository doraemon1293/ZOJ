import sys
for x in sys.stdin.readlines()[1::]:
    if int(x.strip().split()[0])>=int(x.strip().split()[1]):
        print "MMM BRAINS"
    else:
        print "NO BRAINS" 