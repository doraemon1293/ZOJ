import sys
sys.stdin=open("test.txt","r")

primes=set()
primes.add(2)
for num in xrange(3,1001,2):
    f=1
    for t in primes:
        if num%t==0:
            f=0
            break
    if f: 
        primes.add(num)
        #print num
#print primes

arr=list(primes)
arr.sort()
for num in sys.stdin.readlines():
    num=int(num)
    ub=num**0.5
    f=0
    for i in arr:
        if i>ub:
            break
        if num%i==0:
            temp=num/i
            tub=temp**0.5
            ff=1
            for j in arr:
                if j>tub:break
                if temp%j==0:
                    ff=0
                    break

            if ff:
                f=1

    if f:
        print "Yes"
    else:
        print "No"

                
                    
                    
          
     
    