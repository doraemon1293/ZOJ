import sys
sys.stdin=open("test.txt","r")
a= [i*i for i in range(1,13)]
for line in sys.stdin.readlines()[1::]:
    start,end=map(int,[x for x in line.strip().split()])
    ans=0
    for i in range(start,end+1):
        if i %100 in a or i%1000 in a:
            ans+=1
    print ans
            
        
     