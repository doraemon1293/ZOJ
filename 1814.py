import sys

#sys.stdin=open('test.txt','r')
n=int(sys.stdin.readline().strip())

while n:
    a=[]
    for k in range(n):
        a.append(int(sys.stdin.readline().strip()))
    round=0
    while a.count(a[0])!=n:
        round+=1
        b=[0]*n
        for i in range(len(a)):
            if a[i]%2==0:
                if i==n-1:
                    b[0]+=a[i]/2
                else:
                    b[i+1]+=a[i]/2
                b[i]-=a[i]/2
            else:
                b[i]+=1
        a=map(lambda x,y:x+y if (x+y)%2 ==0 else x+y+1 ,a,b)
        #print round
        #print a
    print round,a[0]
    n=int(sys.stdin.readline().strip())
    

    
    