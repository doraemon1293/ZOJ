import sys
from collections import Counter

#sys.stdin=open("test.txt","r")
for line in sys.stdin.readlines():
    s=list(line.strip())
    d=Counter(s)
    s=[x for x in s if x not in ['Z','O','J','7']]
    print ''.join( ['Z']*d['Z']+['O']*d['O']+['J']*d['J']+['7']*d['7']+s)
    
    
        
        
        