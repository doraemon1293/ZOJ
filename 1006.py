import sys
def code(c):
    if c=='_':
        return 0
    elif c=='.':
        return 27
    else:
        return ord(c)-ord('a')+1

def decode(n):
    if n==0:
        return '_'
    elif n==27:
        return'.'
    else:
        return chr(ord('a')+n-1)
for line in sys.stdin.readlines():
    key=int(line.strip().split(' ')[0])
    if key!=0:
        ctext=line.strip().split(' ')[1]
    else:
        break
    ptext=['' for i in range(len(ctext))]
    for i in range(len(ctext)):
        ptext[key*i % len(ctext)]=(code(ctext[i])+i)%28
    print ''.join([decode(n) for n in ptext])
    