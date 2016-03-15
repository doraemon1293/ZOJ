import sys
#sys.stdin=open("test.txt","r")
for line in sys.stdin.readlines()[1::]:
    line=line.strip()+"*"
    old=""
    count=0
    ans=""
    for i in line:
        if old!=i:
            if count>1:
                ans+=str(count)+old
            elif count==1:
                ans+=old
            old=i
            count=1
        else:
            count+=1
    print ans
            
        