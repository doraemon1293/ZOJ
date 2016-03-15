import sys
sys.stdin=open('test.txt','r')

for line in sys.stdin.readlines()[1:]:
    n=int(line)
    print n/2*(n/2 - 1)/2 + (n+1)/2* ((n+1)/2 - 1)/2