import sys
#sys.stdin=open('test.txt','r')
t=int(sys.stdin.readline())
for tt in range(t):
    n,m,k=map(int,sys.stdin.readline().strip().split())
    d={}
    for i in range(n):
        d[i]=set()
    for i in range(m):
        a,b=map(int,sys.stdin.readline().strip().split())
        d[a].add(b)
        d[b].add(a)
    f=1
    ans=0
    while f:
        f=0
        for i in range(n):
            for j in range(i+1,n):
                temp=d[i]&d[j]
                if len(temp)>=k:
                    if i not in d[j]:
                        d[j].add(i)
                        d[i].add(j)
                        ans+=1
                        f=1
                        
    print ans
                    