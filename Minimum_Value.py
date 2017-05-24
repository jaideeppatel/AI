import sys
import queue


minvalue = sys.maxsize
print(minvalue)
# Program Execution starts here .....
print('Enter the Input array')
userinput=input()
inputarray=[]
for items in userinput.split(' '):
    inputarray.append(int(items))
print(userinput)
print(inputarray)
for values in inputarray:
    if values < minvalue:
        minvalue = values
print("Min value is",minvalue)