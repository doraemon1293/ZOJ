import sys
sys.stdin=open("test.txt","r")
t=int(sys.stdin.readline())
for tt in range(t):
    n,s=sys.stdin.readline().strip().split()
    n=int(n)
    a=sys.stdin.readline().strip().split()
    print a[ (a.index(s)+n/2) % n]
    