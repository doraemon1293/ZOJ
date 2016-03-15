import sys
#sys.stdin=open("test.txt","r")
#sys.stdout=open("test.py","w+")
lines=[x.strip() for x in sys.stdin.readlines()]
blocks=int(lines[0])
for line in lines[1::]:
    if line.strip()!="":
        n=int(line.strip())
        if n!=0:
            sum=0
            i=0
            ans=0
            while (sum+i+1)<=n:
                i+=1
                sum+=i
                ans+=i*i
            #print sum,i
            ans+=(i+1)*(n-sum)
            print "%d %d" %(n,ans)
        else:
            blocks-=1
            if blocks:
                print