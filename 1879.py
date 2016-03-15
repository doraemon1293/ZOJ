import sys
lines=[x.strip().split() for x in sys.stdin.readlines()]
for line in lines:
    a=line
    if a[0]==1:
        print "Jolly"
    else:
        b=[abs(a[i+1]-a[i]) for i in range(1,a[0])]
        flag=0
        
        for i in range(1,a[0]):
            if b.count(i)!=1:
                print "Not jolly"
                flag=1
                break
        if flag==0:
            print "Jolly"
        #print b

        