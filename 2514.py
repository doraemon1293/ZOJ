import sys
#sys.stdin=open("test.txt","r")
n=int(sys.stdin.readline())
while n:
    ans=[]
    for i in xrange(n):
        name,pwd= sys.stdin.readline().strip().split(' ')
        newPwd=pwd.replace('1','@').replace('0','%').replace('l','L').replace('O','o')
        if newPwd!=pwd:
            ans.append( name+' '+newPwd )
    if ans==[]:
        print "No account is modified."
    else:
        print len(ans)
        for x in ans:
            print x
    n=int(sys.stdin.readline())

            
        