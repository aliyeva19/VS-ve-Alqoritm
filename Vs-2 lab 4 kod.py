x=int(input())
y=int(input())
n=12
a=[0]*n


k=0
s=0


from random import randint
for i in range(n):
    a[i]=randint(x,y)
print('A',a)
for k in range(len(a)):
    if k%2==1:
        s=s+a[k]
        k=k+1
print(s)
