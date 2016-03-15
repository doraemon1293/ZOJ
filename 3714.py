import sys
#sys.stdin=open('test.txt','r')
t=int(sys.stdin.readline())
def f(i,a):
    start=i
    end=i+m
    if end<=n:
        return sum(a[start:end])
    else:
        return sum(a[start:n])+sum(a[:m-n+start])


for tt in range(t):
    n,m=map(int,sys.stdin.readline().strip().split())
    a=map(int,sys.stdin.readline().strip().split())
    print max( [f(i,a) for i in range(n)])

    