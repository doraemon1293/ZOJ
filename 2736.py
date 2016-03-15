import sys
#sys.stdin=open("test.txt","r")
for line in sys.stdin.readlines():
    if sum( map(lambda x:x**3,[int(x)for x in line.strip()]) )==int(line.strip()):
        print "Yes"
    else:
        print "No"