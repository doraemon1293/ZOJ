import sys
for line in sys.stdin.readlines()[:-1:]:
    sum=0
    for k,num in enumerate(line.strip()[::-1]):
        num=int(num)
        #print num
        sum+=(2**(k+1)-1)*num
    print sum
    
        
        