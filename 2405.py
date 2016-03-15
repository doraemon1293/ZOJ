
for n in range(2992,10000):
    
    tempn=n
    sum10=0
    while tempn:
        sum10+=tempn%10
        tempn/=10
    
    tempn=n
    sum12=0
    while tempn:
        sum12+=tempn%12
        tempn/=12
    
    if sum10!=sum12:
        continue
    
    tempn=n
    sum16=0
    while tempn:
        sum16+=tempn%16
        tempn/=16        
    if sum12!=sum16:
        continue
    print n
        