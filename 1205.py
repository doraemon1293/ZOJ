import sys

def code(num):
    if num.isdigit():
        return int(num)
    else:
        return ord(num)-ord('a')+10

def decode(num):
    if num<10:
        return str(num)
    else:
        return chr(num-10+ord('a'))

def add(a,b):
    ans=[]
    add=0
    
    for i in range( max(len(a),len(b)) ):
        if i<len(a):
            numa=code(a[i])
        else:
            numa=0
        if i<len(b):
            numb=code(b[i])
        else:
            numb=0
        sum=numa+numb+add
        c=decode(sum%20)
        add=sum/20
        ans.append(c)
    if add==1:
        ans.append('1')
    if ans==[]:
        return ['0']
    else:
        return ans[::-1]
    
lines=[x.strip().lstrip('0') for x in sys.stdin.readlines()]

for i in range(len(lines))[::2]:
    a=lines[i][::-1]
    b=lines[i+1][::-1]
    print ''.join( add(a,b) )

