import sys
#sys.stdin=open("test.txt","r")
windows=int(sys.stdin.readline())
a= [ [int(x) for x in sys.stdin.readline().strip().split()] for i in xrange(windows)  ] 
clicks=int(sys.stdin.readline())
for i in xrange(clicks):
    x,y=[int(x) for x in sys.stdin.readline().strip().split()]
    f=0
    for n,w in enumerate(a[::-1]):
        if w[0]<=x and w[2]>=x and w[1]<=y and w[3]>=y:
            f=1
            print windows-1-n
            break
    if f==0:
        print -1
        
    
    