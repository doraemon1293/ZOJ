import sys
#sys.stdin=open("test.txt","r")
n=int(sys.stdin.readline())
while n:
    s=sys.stdin.readline().strip()
    m=len(s)/n
    a=[]
    for i in range(m):
        if i%2==0:
            a.append(s[i*n:i*n+n])
        else:
            a.append(s[i*n:i*n+n][::-1])

    ans=""
    for j in range(n): 
        for i in range(m):
            ans+=a[i][j]
    print ans
    n=int(sys.stdin.readline())
