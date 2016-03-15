import sys

lines=[s.strip() for s in sys.stdin.readlines()]

a={}
i=0
j=0
x=0
add=[[1,1],[1,-1],[1,1],[-1,1]]
t=0
while (i<5001 and j <5001):
    
    a[' '.join([str(i),str(j)])]=x
    x+=1
    i+=add[t][0]
    j+=add[t][1]
    t=(t+1)%4

for line in lines[1::]:
    if line in a:
        print a[line]
    else:
        print "No Number"

