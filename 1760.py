import sys
for line in sys.stdin.readlines()[:-1:]:
    arr= [int(x) for x in line.strip().split()[:-1:]]
    arr1=[2*x for x in arr]
    ans=0
    for x in arr:
        if x in arr1:ans+=1
    print ans
            

    
    