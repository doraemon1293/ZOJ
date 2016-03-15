import sys
#sys.stdin=open("test.txt","r")
for line in sys.stdin.readlines()[1::]:
    d,t=map(int,line.strip().split())
    
    if d<3:
        a=11
    elif d<=10:
        a=11+(d-3)*2
    else:
        a=25+(d-10)*3
    a+=0.4*t
    a=round(a)
    b=0
    if d<3:
        b=11
    elif d<=10:
        b=11+(d-3)*2.5
    else:
        b=28.5+(d-10)*3.75
    b+=t*0.625
    b=round(b)
    print int( b-a )
    