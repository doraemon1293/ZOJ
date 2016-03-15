import sys

a=r"1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./"
for line in sys.stdin.readlines():
    ans=[]
    line=line.strip('\r\n')
    for i in line:
        if i in ['1','Q','A','Z',' ']:
            ans.append(i)
        else:
            ans.append(a[a.index(i)-1])
    print ''.join(ans)