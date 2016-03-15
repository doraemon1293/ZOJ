import sys




lines=[x.strip() for x in sys.stdin.readlines()]

for line in range(len(lines))[::2]:
    num=int(lines[line])
    
    if num==0:break
    
    arr=lines[line+1].split(' ')
    ans=[0]*num
    if arr[0]=='P':
        arr.pop(0)
        arr=[int(x) for x in arr]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]>arr[j]:
                    ans[arr[j]-1]+=1
    elif arr[0]=='I':
        arr.pop(0)
        arr=[int(x) for x in arr]
        for i in range(len(arr)):
            temp=0
            j=0
            while temp<=arr[i]:
                if ans[j]==0:
                    temp+=1
                j+=1
            ans[j-1]=i+1
    print ' '.join([str(x) for x in ans])
                
        
                    
        
    
