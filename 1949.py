import sys
#sys.stdin=open("test.txt","r")
n=int(sys.stdin.readline().strip())
while n:
    a=[]
    for i in range(n):
        a.append([int(x) for x in sys.stdin.readline().strip().split()])
    nRow=0
    nCol=0
    
    for i in range(n):
        if sum(a[i])%2:
            nRow+=1
            row=i
            if nRow>1:
                break
        if sum(x[i] for x in a)%2:
            nCol+=1
            col=i
            if nCol>1:
                break
    if nRow==0 and nCol==0:
        print "OK"
    elif nRow==1 and nCol==1:
        print "Change bit (%d,%d)" %(row+1,col+1)
    else:
        print "Corrupt"
    n=int(sys.stdin.readline().strip())


    
            
    