import sys
import queue
import math

a = [22,45,12,8,9,10,6,72,81,7,33,18,5,50,14]
n = len(a)
b = [None]*5
m = len(b)
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
divider = math.ceil((max+1)/m)

j=0
for j in range(0,n):
    index = math.floor(a[j]/divider)
    if b[index]==None:
        item = [a[j]]
        b[index]=item
    else:
        flag=0
        for items in b[index]:
            if a[j]<items:
                # print('items and aj',items,a[j],b[index])
                flag=1
                xx = b[index].index(items)
                temp = b[index][:xx]+[a[j]]+b[index][xx:]
                b[index] = temp
                print("appeded b is:",b[index])
                break
        if flag==0:
            b[index].append(a[j])

print("Filled Bucket List is:",b)

result = []
for vals in b:
    if vals!=None:
        for elements in vals:
            result.append(elements)

print("Sorted Array is:",result)