import sys
import copy
sys.stdin=open('test.txt','r')
t=int(sys.stdin.readline())
dict={0:'.',1:'!',2:'X',3:'#'}

def density(i,j):
    temp=a[i][j]
    temp+=a[i-1][j] if i-1>=0 else 0
    temp+=a[i][j-1] if j-1>=0 else 0
    temp+=a[i+1][j] if i+1<20 else 0
    temp+=a[i][j+1] if j+1<20 else 0
    temp=a[i][j]+d[temp]
    temp=temp if temp>=0 else 0
    temp=temp if temp<=3 else 3
    return temp
    
 
for tt in range(t):
    sys.stdin.readline()
    days=int(sys.stdin.readline())
    d=map(int,sys.stdin.readline().strip().split())
    a=[]
    
    
    for i in range(20):
        a.append( map(int,sys.stdin.readline().strip().split()) )
    for day in range(days):
        b=[ [0]*20 for i in range(20) ]
        for i in range(20):
            for j in range(20):
                b[i][j]=density(i, j)
        a=copy.copy(b)
    
    for i in range(20):
            print ''.join(map(lambda x:dict[x], a[i]))
            #print ''.join(str(a[i]))
                
    if tt!=t-1:
        print
    