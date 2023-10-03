from random import randint
n=int(input('n='))
a=[0]*n
p=1
for i in range(n):
    a[i]=randint(-12,24)
    if a[i]<0:
        p=p*a[i]
if p==1:
    print('a=',a,'\n','hasil=0')
else:
    print('a=',a,'\n','hasil=',p)
