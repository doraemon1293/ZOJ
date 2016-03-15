import sys
#sys.stdin=open('test.txt','r')

for line in sys.stdin.readlines()[:-1]:
    a=map(int,line.strip().split()[:-1])
    
    length=0
    up=0.0
    down=0.0
    flag=0
    type=0
    countUp=0
    countDown=0
    for i in range(1,len(a)):
        if type==0:
            if a[i]==a[i-1]:
                length+=1
            if a[i]>a[i-1]:
                type=1
                length+=1
                countUp+=1
            if a[i]<a[i-1]:
                type=2
                length+=1
                countDown+=1
                
        elif type==1:
            if a[i]<a[i-1]:
                up+=length
                type=2
                length=1
                countDown+=1
            else:
                length+=1
                
        elif type==2:
            if a[i]>a[i-1]:
                down+=length
                countUp+=1
                length=1
                type=1
            else:
                length+=1
                
    if type==1:
        up+=length
    elif type==2:
        down+=length
    if countUp!=0:
        up/=countUp
    if countDown!=0:
        down/=countDown
    print "Nr values = %d:  %.6f %.6f" %(len(a),up,down)
    
            
            

                
                





