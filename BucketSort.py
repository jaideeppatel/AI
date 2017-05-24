import sys
import queue
import math

a = [22,45,12,8,10,6,72,81,33,18,50,14]
n = len(a)
b = [None]*10
i=0
min = a[0]
max = a[0]
for i in range(1,n):
    if a[i]<min:
        min = a[i]
    if a[i]>max:
        max = a[i]

print("min,max,t values are:",min,max,n)
print("Bucket list is:",b)
j=0
divider = math.ceil((max+1)/10)

for j in range(0,n):
    index = math.floor(a[j]/divider)
    print('Index:',index,a[j])
    if b[index]==None:
        item = [a[j]]
        b[index]=item
    else:
        b[index].append(a[j])
    print('b is:',b)
print(b)
print("Filled Bucket List is:",b)
x=0
for items in b:
    i=0
    j=1
    if items!=None:
        for i in range(0,len(items)):
            for j in range(i+1,len(items)):
                if items[i]>items[j]:
                    print(items[i],items[j])
                    print(x,i,j)
                    temp = b[x][i]
                    b[x][i]=b[x][j]
                    b[x][j]=temp
                    print("b is:",b)
    x=x+1


