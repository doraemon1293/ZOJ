import sys
#sys.stdin=open('test.txt','r')
lines=sys.stdin.readlines()

sub=lines[0].rstrip('\r\n')
plain=lines[1].rstrip('\r\n')
text=[x.rstrip('\r\n') for x in lines[2::]]
d={}
for i,c in enumerate(sub):
    d[c]=plain[i]
print plain
print sub 
for line in text:
    print ''.join( [d[x] if x in d else x for x in line] )
    
    
