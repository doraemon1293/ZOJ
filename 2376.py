import sys
sys.stdin=open('test.txt','r')
testcases=int(sys.stdin.readline())
for testcase in range(testcases):
    while True:
        line=sys.stdin.readline().strip()
        if line!="":
            break
    length,n=map(int,line.split())
    while True:
        line=sys.stdin.readline().strip()
        if line!="":
            break
    pos=map(int,line.split())
    a=[]
    b=[]
    if pos:
        for t in pos:
            a.append(min(t,length-t))
            b.append(max(t,length-t))
        print max(a),max(b)
    else:
        print 0,0
    
    