import sys
for line in sys.stdin.readlines()[:-1]:
    n=int(line)
    if n>=8:
        ans=n/8*18
        ans+= n%8*2.4 if n%8 <=4 else 10+(n%8-4)*2
    else:
        ans=10 if n<=4 else 10+(n-4)*2
    if ans==int(ans):
        print int(ans)
    else:
        print "%.1f" %ans
    
    
