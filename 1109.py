import sys
d={}
step=0
for line in sys.stdin.readlines():
    line=line.strip()
    if step==0:
        if line=="":
            step=1
            continue
        word,key=line.split(' ')
        d[key]=word
    if step==1:
        if line in d:
            print d[line]
        else:
            print "eh"


