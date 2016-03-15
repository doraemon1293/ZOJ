import sys
for line in sys.stdin.readlines():
    
    num=int(line.strip())
    if num==0:break
    sum=999
    while sum>=10:
        sum=0
        while num>0:
            sum+=num % 10
            num/=10
        
        if sum>=10: num=sum
    print sum
            