import sys

for line in sys.stdin:
    sum=float(line)
#sum=1.0
    if sum==0: break
    temp=0;
    n=0;
    while (temp<sum):
        temp+=1/(n+2.0)
        n+=1
    print str(n)+" card(s)"
        
        