import sys
sys.stdin=open("test.txt","r")
def f(n):
    if n==1:
        return 0
    if n==2:
        return 1
    if n%2==0:
        return 1+f(n/2)
    if n%2==1:
        return 1+f( (n-1)/2+1 )

for n in sys.stdin.readlines()[:-1:]:
    print f(int(n))