def d(num):
    sum=num;
    while num>0:
        sum+=num%10
        num/=10
    return sum


ans=[False for i in range(1000000)]
print ans
for i in range(1000000):
    if d(i)<1000000:
        ans[d(i)]=True
for i in range(1000000):
    if ans[i]==False:print i
