import sys
#sys.stdin=open("test.txt","r")
s=sys.stdin.readline().strip()
while s!='#':
    sum=0
    for i,c in enumerate(s):
        sum+=(i+1)*(ord(c)-ord('A')+1) if c!=' ' else 0
        #print c,ord(c)-ord('A')
    print sum
    s=sys.stdin.readline().strip()

        
    
    