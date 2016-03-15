import sys
lines=[x.strip() for x in sys.stdin.readlines()[:-1:]]
start=0

while start<len(lines):
    end=int(lines[start])+start
    max=0
    min=sys.maxint
    for line in lines[start+1:end+1]:
        v=reduce(lambda x,y:x*y, [ int(x) for x in line.split()[0:3] ])
        
        if v>max:
            max=v
            bully=line.split()[3]
        if v<min:
            min=v
            victim=line.split()[3]
    print "%s took clay from %s."%(bully,victim)
    start=end+1

        
        
    