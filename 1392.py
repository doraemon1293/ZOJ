import sys

lines=[s.strip('\n\r') for s in sys.stdin.readlines()]

def decode(c):
    if c.isupper():
        c=chr( ord(c)-5 ) if ord(c)-5 >=ord('A') else chr( ord(c)-5+26)
        return c
    else:
        return c
for s in lines:
    if s!="START" and s!="END" and s!="ENDOFINPUT":
        s=[decode(c) for c in s]
        #print s
        print ''.join(s)