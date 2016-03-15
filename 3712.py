import sys
#sys.stdin=open('test.txt','r')
t=int(sys.stdin.readline())
for tt in range(t):
    a,b,c=map(int,sys.stdin.readline().strip().split())
    combo=0
    min=0
    max=0
    for i in range(a):
        min+=300*(combo*2+1)
        combo+=1
    for i in range(b):
        min+=100*(combo*2+1)
        combo+=1
    for i in range(c):
        min+=50*(combo*2+1)
        combo+=1
    combo=0
    for i in range(c):
        max+=50*(combo*2+1)
        combo+=1
    for i in range(b):
        max+=100*(combo*2+1)
        combo+=1
    for i in range(a):
        max+=300*(combo*2+1)
        combo+=1
    print min,max