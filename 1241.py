import sys
lines=[x.strip() for x in sys.stdin.readlines()]
for line in range(len(lines)):
    a,b,c=[int(x) for x in lines[line].split()]
    #impoossible=False
    if a==0 and b==0 and c==0:break
    
    if a==-1:
        if c>b:
            x=c**2-b**2
            ch='a'
            ans=ch+" = %.3f" %(x**0.5)
        else:
            ans="Impossible."
    elif b==-1:
        if c>a:
            x=c**2-a**2
            ch='b'
            ans=ch+" = %.3f" %(x**0.5)
        else:
            ans="Impossible."
    elif c==-1:
            x=a**2+b**2
            ch='c'
            ans=ch+" = %.3f" %(x**0.5)

    print "Triangle #%d" %(line+1)
    print ans
    print 
        
    