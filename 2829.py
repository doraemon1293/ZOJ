import sys
sys.stdin=open("test.txt","r")

a=[]
for i in xrange(1,300000):
    if i%3==0 or i%5==0:
        a.append(i)
for line in sys.stdin.readlines():
    n=int(line)
    print a[n-1]