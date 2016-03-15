import sys
p=[
["Wide Receiver",    4.5,    150,    200],
["Lineman",    6.0,    300,    500],
["Quarterback",    5.0,    200,    300]
]
#sys.stdin=open("test.txt","r")
for line in sys.stdin.readlines()[:-1:]:
    speed,weight,strength=[float(x) for x in line.strip().split()]
                           
    ans=[]
    for i in range(3):
        if p[i][1]>=speed and weight>=p[i][2] and strength>=p[i][3]:
            ans.append(p[i][0])
    if ans==[]:
        print "No positions"
    else:
        print ' '.join(ans)
        
        
    