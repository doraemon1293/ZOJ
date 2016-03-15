import sys

def f(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return f(n-1)+2*f(n-2)+1
#sys.stdin=open("test.txt","r")
testcases=int(sys.stdin.readline())
for testcase in range(testcases):
    n=int(sys.stdin.readline())
    print f(n)