import sys
for n in sys.stdin.readlines():
    n=int(n)
    ans=1
    m=1
    while m%n:
        m=(m*10+1)%n
        ans+=1
    print ans
    
        
    