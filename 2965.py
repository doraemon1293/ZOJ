import sys
sys.stdin=open("test.txt","r")

a=[None]*200
min=0
start=-1

for n in range(1,800):
    if n%7==0 or '7' in str(n):
        if start==-1:
            start=n
        end=n
        if end-start+1>min:
            #print min,start
            min=end-start+1
            a[min]=start
        
    else:
        start=-1
            
        
for x in sys.stdin.readlines()[1::]:
    print a[int(x)]
    
    





