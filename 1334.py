import sys
#sys.stdin=open('test.txt','r')
for line in sys.stdin.readlines():
    a,b1,b2=line.strip().split()
    a=a[::-1]
    b1=int(b1)
    b2=int(b2)
    num=0
    for n,i in enumerate(a):
        if i.isdigit():
            temp=int(i)
        else:
            temp=ord(i)-ord('A')+10
        temp*=b1**n
        num+=temp
    ans=[]
    while num:
        temp=num%b2
        if temp>=10:
            temp=chr(65+temp-10)
        else:
            temp=str(temp)
        ans.append(temp)
        num/=b2
    ans=ans[::-1]
    ans=''.join([x for x in ans])
    if len(ans)>7:
        ans="ERROR"
    print "% 7s"%ans
        
        
        