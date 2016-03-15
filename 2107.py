import sys
sys.stdin=open("test.txt","r")
n=int(sys.stdin.readline().strip())
while n:
    a=[]
    
    for i in range(n):
        x,y=[float(x) for x in sys.stdin.readline().strip().split()]
        if a!=[]:
            d=min([ (j[0]-x)**2+(j[1]-y)**2 for j in a])
        a.append([x,y])
    print "%.2f" %((d**0.5)/2)
    n=int(sys.stdin.readline().strip())

        
        