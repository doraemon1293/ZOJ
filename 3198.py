import sys
#sys.stdin=open("test.txt","r")
testcases=int(sys.stdin.readline())
for testcase in range(testcases):
    n0=int(sys.stdin.readline())
    a0=[]
    for i in range(n0):
        a0.append(int( sys.stdin.readline()))
    
    n1=int(sys.stdin.readline())
    a1=[]
    for i in range(n1):
        a1.append(int (sys.stdin.readline()))
    i=0
    j=0
    ans=0
    
    while i<n0 and j<n1:
        if a0[i]==a1[j]:
            ans+=1
            i+=1
            j+=1
        elif a0[i]>a1[j]:
            j+=1
        else:
            i+=1
    print ans
            
            
         
    