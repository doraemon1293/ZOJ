import sys

def add(a,b):
    ans=[]

    add=0
    
    for i in range( max(len(a),len(b)) ):
        if i<len(a):
            numa=int(a[i])
        else:
            numa=0
        if i<len(b):
            numb=int(b[i])
        else:
            numb=0
        sum=numa+numb+add
        c=sum%10
        add=sum/10
        ans.append(str(c))
    if add==1:
        ans.append('1')
    if ans==[]:
        return ['0']
    else:
        return ans

lines=[x.strip() for x in sys.stdin.readlines()]
blocks=int(lines[0])
block=0
nums=[]
for line in lines[1::]:
    if line!='':
        nums.append(line.lstrip('0')[::-1])
    if line=='0':
        print ''.join( reduce(add,nums)[::-1] )
        nums=[]
        block+=1
        if block!=blocks:
            print