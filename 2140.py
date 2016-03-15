import sys
lines=sys.stdin.readlines()
num=int(lines[0].strip())
for i in range(1,num+1):
    s=[chr(ord(x)+1) if x!='Z' else 'A' for x in lines[i].strip()]
    print "String #%d" %i
    print ''.join(s)
    print


    