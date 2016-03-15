import sys
lines=[x.strip() for x in sys.stdin.readlines()]
for line in range(len(lines))[::2]:
    
    if int(lines[line])==0:
        break
    else:
        num=[int(x) for x in lines[line+1].split(' ')]
    ave=sum(num)/len(num)
    ans=0
    for i in num:
        ans+=i-ave if (i-ave)>0 else 0
    print "Set #%d" %((line+2)/2)
    print "The minimum number of moves is %d." %ans
    print 

    
        
