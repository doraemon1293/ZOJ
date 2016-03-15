import sys
lines=[int(x.strip()) for x in sys.stdin.readlines()]
print "# Cards  Overhang"
for num in lines:
    ans=0.0
    for i in range(1,num+1):
        ans+=1.0/(2*i)
    print "%5d%10.3f" %(num,ans)
    