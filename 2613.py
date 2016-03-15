import sys
#sys.stdin=open("test.txt","r")

t=int( (sys.stdin.readline()) )
for tt in xrange(t):
    sys.stdin.readline()
    u,m=map(int,sys.stdin.readline().strip().split())
    d={}
    for mm in xrange(m):
        name,price= sys.stdin.readline().strip().split()
        price=int(price)
        if price<=u:
            if price not in d:
                d[price]=[name,1]
            else:
                d[price][1]+=1
    minCounts=sys.maxint
    minPrice=sys.maxint
    for key in d:
        if minCounts>d[key][1]:
            minCounts=d[key][1]
            minPrice=key
            winner=d[key][0]
        elif minCounts==d[key][1]:
            if key<minPrice:
                minPrice=key
                winner=d[key][0]
    print "Case %d:" %(tt+1)
    print "The winner is %s." %winner
    print "The price is %d." %minPrice
    if tt!=t-1: print

                
            
            
        
