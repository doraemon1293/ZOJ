import sys
        
#sys.stdin=open("test.txt","r")
testcases=int(sys.stdin.readline())
for testcase in range(testcases):
    start,end=map(int,sys.stdin.readline().strip().split())
    
    s1=sum(range(start,end+1))
    
    a=[]
    for i in range(8):
        a.append(list(sys.stdin.readline().strip())[::-1])
    s2=0
    for i in range(6):
        temp=0
        if a[1][i]=='o':
            temp+=5
        x=3
        while a[x][i]=='o':
            temp+=1
            x+=1
        temp*=10**i
        s2+=temp
    if s1==s2:
        print "No mistake"
    else:
        print "Mistake"
    if testcase!=testcases-1:
        sys.stdin.readline()
        
        
