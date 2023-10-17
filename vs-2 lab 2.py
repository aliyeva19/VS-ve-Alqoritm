#15 İki ölçülü A(n,m) ədədi massivinin hər bir sütunundakı mənfi elementlərinin hasilini hesablayan alqoritm tərtib etməli.

import random
def printList(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(lst[i][j],end='       ')
        print()

p=1
n=5
m=5
a=[]
z=[]
for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append(random.randint(-5,10))
printList(a)
for i in range(n):
    for j in range(m):
        if a[j][i]<0:
            p=p*a[j][i]
            z.append(a[j][i])
                       
print('Z=',z,'\n','hasil=',p)
