import sys
lines=[int(x.strip()) for x in sys.stdin.readlines()]
for n in lines[1::]:
    p=0
    while n%2==0 :
        n/=2
        p+=1
    print n,p