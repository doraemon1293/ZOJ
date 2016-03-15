import sys
from math import log
#sys.stdin=open('test.txt','r')
s=0
for line in sys.stdin.readlines()[:-1:]:
    s+=1
    y=map(float,line.strip().split())[1]/map(float,line.strip().split())[0]
    y=810/y
    x=log(y,2)
    #print x
    ans=5730*x
    if ans<10000:
        ans= int(round(ans,-2))
    else:
        ans= int(round(ans,-3))
    
    
    
    print "Sample #%d" %s
    print "The approximate age is %d years." %ans


    