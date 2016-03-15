import sys
sys.stdin=open('test.txt','r')
t=int(sys.stdin.readline())
    
for tt in range(t):
    n,m=map(int,sys.stdin.readline().strip().split())
    a1=sum( map(int,sys.stdin.readline().strip().split()) )
    a2=sum( map(int,sys.stdin.readline().strip().split()) )
    if a1>a2:
        print "Calem"
    elif a1<a2:
        print "Serena"
    else:
        print "Draw"
        