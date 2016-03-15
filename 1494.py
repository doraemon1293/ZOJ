import sys
lines=[s.strip() for s in sys.stdin.readlines()]

for line in lines[:-1:]:
    n,u,d=[int(x) for x in line.split(' ')]
    climb=0
    minutes=0
    while climb<n:
        minutes+=1
        if minutes%2==1:
            climb+=u
        elif minutes%2==0:
            climb-=d
    print minutes
            