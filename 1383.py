import sys
lines=[int(x.strip()) for x in sys.stdin.readlines()]


for num in lines[1::]:
    ans=[]
    i=0
    while num!=0:
        if num%2:
            ans.append(str(i))
        num/=2
        i+=1
    print ' '.join(ans)
    