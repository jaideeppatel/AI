import sys
import queue
import math


print('Enter the Input array')
userinput=input()
a=[]
for items in userinput.split(' '):
    a.append(int(items))
print(a)
fact=1
sum=0
prod=1
nonzeroprod=1
netprod=1
n = len(a)
i=0
max=n+1

for i in range(n):
    sum+=a[i]
    prod*=a[i]
    if a[i]==0:
        nonzeroprod*=1
    else:
        nonzeroprod*=a[i]
    if max<a[i]:
        max=a[i]
while(max>=1): ##product of all the number (includes missing number)
    fact*=max
    max = max-1
netsum=((n+1)*(n+2))/2 - sum ##the sum of the 2 missing numbers
print(sum,netsum,prod,nonzeroprod,fact)
if prod==0:
    nonzeroprod = fact/nonzeroprod
    x=netsum/2 + math.sqrt(netsum*netsum - 4*nonzeroprod)/2
    y=netsum/2 - math.sqrt(netsum*netsum - 4*nonzeroprod)/2
else:
    x = 0
    y = netsum
print(x,y)