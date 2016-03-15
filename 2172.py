import sys
#sys.stdin=open('test.txt','r')
n=int(sys.stdin.readline())
num=0
while n:
    num+=1
    a=[]
    for i in range(n):
        a.append(sys.stdin.readline().strip())
    b=[None]*n
    for i,name in enumerate(a):
        if i%2==0:
            b[i/2]=name
        else:
            b[-(i/2+1)]=name
    print "SET %d"%(num)
    for name in b:
        print name
    n=int(sys.stdin.readline())

            
        