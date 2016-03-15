import sys
lines=[int(x.strip()) for x in sys.stdin.readlines()]
num=lines[0]
line=1
while num!=0:
    a=[]
    for i in range(line,line+num):
        a.append(lines[i])
    a.sort()
    
    x=0
    y=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            flag=False
            m=a[i]
            n=a[j]
            
            while m:
                temp=n%m
                n=m
                m=temp
            if n==1:
                flag=True
            if flag:
                y+=1
            x+=1
    line+=num
    num=lines[line]
    line+=1
    
    if y==0:
        print "No estimate for this data set."
    else:
        pi=(6.0*x/y)**0.5
        print "%.6f" %pi
            