import sys

def lcm(a,b):
    aa=a
    bb=b
    if a<b:
        temp=b
        b=a
        a=temp
    while a%b != 0:
        temp=a
        a=b
        b=temp%b
    #print aa,bb,b
    return aa*bb/b
        
lines = [x.strip() for x in sys.stdin.readlines()[1::]]
for line in lines:
    arr=[int(x) for x in line.split()[1::]]
    print reduce(lcm,arr)
    

