import sys
#sys.stdin=open("test.txt","r")
n=int(sys.stdin.readline())
while n!=-1:
    ans=0
    t0=0
    for i in range(n):
        s,t=[int(x) for x in sys.stdin.readline().strip().split()]
        ans+=s*(t-t0)
        t0=t
    print ans,"miles"
    n=int(sys.stdin.readline())
