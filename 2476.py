import sys
#sys.stdin=open("test.txt","r")
sum=0
for line in sys.stdin.readlines()[1::]:
    
    if line[0]=='$':
        line=float( line.strip().replace(',','')[1::] )
        sum+=line
    else:
        print "$"+format(sum,',.2f')
        sum=0
        
        