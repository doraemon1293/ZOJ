import sys
def code(c):
    if c in ['B','F','P','V']:
        return '1'
    elif c in ['C', 'G','J','K','Q','S','X','Z']:
        return '2'
    elif c in ['D','T']:
        return '3'
    elif c in ['L']:
        return '4'
    elif c in ['M','N']:
        return '5'
    elif c in ['R']:
        return '6'
    else:
        return ''
for line in sys.stdin.readlines():
    ans=[]
    s=line.strip()
    for i,c in enumerate(s):

        if len(ans)==0:
            ans.append(code(c))
        else:
            if code(c)!=ans[-1]:
                ans.append(code(c))
    print ''.join(ans)
    
            
    