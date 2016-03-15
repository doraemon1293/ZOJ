import sys
#sys.stdin=open('test.txt','r')
t=int(sys.stdin.readline())
def f(a,b,c):
    s=set([0,
           a,b,c,
           a+b,abs(a-b),b+c,abs(b-c),a+c,abs(a-c),
           abs(a+b-c),abs(a+c-b),abs(b+c-a),
           a+b+c])
    return len(s)-1
       
    
for tt in range(t):
    x,y=map(int,sys.stdin.readline().strip().split())
   
    masses=0
    for i in range(x+1):
        temp=f(i,x-i,y)
        if temp>masses:
            masses=temp
    for i in range(y+1):
        temp=f(i,y-i,x)
        if temp>masses:
            masses=temp
    print masses
   
       
       
       
       