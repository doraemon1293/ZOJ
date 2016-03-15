import sys
#sys.stdin=open('test.txt','r')
lines=sys.stdin.readlines()[:-1]
for line in lines:
    a1,b1,a2,b2,a3,b3=map(int,line.strip().split())
    t1=b1+b2+b3-a1-a2-a3
    t2=a1+b1
    a=(t1+t2)/2
    b=(t2-t1)/2
    print "Anna's won-loss record is %d-%d."%(a,b)
