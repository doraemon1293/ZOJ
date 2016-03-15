import sys
#sys.stdin=open("test.txt","r")
t=int(sys.stdin.readline())
for tt in range(t):
    n,s=sys.stdin.readline().strip().split()
    n=int(n)
    s=s[:n-1:]+s[n::]
    print tt+1,s
    