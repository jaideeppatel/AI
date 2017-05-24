import sys
import queue
import math
#
# def BubbleSort(inputarray):
#     i=0
#     j=0
#     length = len(inputarray)
#     for i in range(0,length):
#         for j in range(length-1-i):
#             if inputarray[j]>inputarray[j+1]:
#                 temp = inputarray[j+1]
#                 inputarray[j+1]=inputarray[j]
#                 inputarray[j]=temp
#         print("Array at current pass:",inputarray)
#
#     print("Final Sorted Array is:",inputarray)
#     return
# #
# def InsertionSort(inputarray):
#     hold=None
#     length = len(inputarray)
#     for i in range(0,length):
#         hold= inputarray[i]
#         j=i
#         while j>0 and inputarray[j-1]>hold:
#             inputarray[j]=inputarray[j-1]
#             j=j-1
#         inputarray[j]=hold
#         print("Array at current pass:",inputarray)
#
#     print('Sorted Array is:',inputarray)

def MergeSort(inputarray,begin,end):
    mid = 0
    if begin<end:
        mid = int((begin+end)/2)
        MergeSort(inputarray,begin,mid)
        MergeSort(inputarray,mid+1,end)
        Merge(inputarray,begin,mid,end)
    else:
        return

def Merge(inputarray,begin,mid,end):
    beginleft = begin
    endleft = mid
    beginright = mid+1
    endright = end
    i=begin
    while beginleft<=endleft and beginright<=endright:
        if inputarray[beginleft]<inputarray[beginright]:
            temp[i]=inputarray[beginleft]
            beginleft=beginleft+1
        elif inputarray[beginleft]>inputarray[beginright]:
            temp[i]=inputarray[beginright]
            beginright=beginright+1
        else:
            print("Else Executed")
            temp[i] = ''
            beginright=beginright+1
        i=i+1
    while beginleft<=endleft:
        temp[i]=inputarray[beginleft]
        beginleft=beginleft+1
        i=i+1
    while beginright<=endright:
        temp[i]=inputarray[beginright]
        beginright=beginright+1
        i=i+1

    x=begin
    for x in range(end+1):
        inputarray[x]=temp[x]
    print('Current pass Array is:',inputarray)

# Program Execution Begins here .....
print("Program Execution Started...")
print('Enter the Input array')
userinput=input()
inputarray=[]
for items in userinput.split(' '):
    inputarray.append(int(items))
print("Input array is",inputarray)
# BubbleSort(inputarray)
# InsertionSort(inputarray)
n = len(inputarray)
temp=[0,0,0,0,0]
MergeSort(inputarray,0,n-1)
print('Final sorted Array is',inputarray)