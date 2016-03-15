import sys
#sys.stdin=open("test.txt","r")
n=int(sys.stdin.readline().strip())
while n:
    d={}
    max=0
    for i in range(n):
        color=sys.stdin.readline().strip()
        if color in d:
            d[color]+=1
        else:
            d[color]=1
        if d[color]>max:
            pop=color
    print pop
    n=int(sys.stdin.readline().strip())

        