import sys
sys.stdin=open('test.txt','r')
t=int(sys.stdin.readline())
d={'+':0, '-':0 , '*':1, '/':1, '%':1}
for tt in range(t):
    s=sys.stdin.readline().strip().split()
    queue=[]
    stack=[]
    for c in s:
        if c.isdigit():
            queue.append(int(c))
        else:
            if stack==[] or stack[-1]<d[c]:
                stack.append(c)
            else:
                while stack!=[] and d[stack[-1]]>=d[c]:
                    queue.append(stack.pop())
                stack.append(c)
    while stack!=[]:
        queue.append(stack.pop())
    #print queue
    for x in queue:
        if type(x) is int:
            stack.append(x)
        else:
            b=stack.pop()
            a=stack.pop()
            if x=='+':
                temp=a+b
            elif x=='-':
                temp=a-b
            elif x=='*':
                temp=a*b
            elif x=='/':
                temp=a/b
            elif x=='%':
                temp=a%b
            stack.append(temp)
    print stack[0]






