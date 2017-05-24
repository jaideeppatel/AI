# Quicksort Sort
def partition(inputarray, low, high):
    i = low-1         # index of smaller element
    pivot = inputarray[high]     # pivot
    for j in range(low , high):
        if   inputarray[j] <= pivot:
            i = i+1
            inputarray[i], inputarray[j] = inputarray[j], inputarray[i]

    inputarray[i + 1], inputarray[high] = inputarray[high], inputarray[i + 1]
    return ( i+1 )

# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

# Program Execution starts here .....
print('Enter the Input array')
userinput=input()
inputarray=[]
for items in userinput.split(' '):
    inputarray.append(int(items))
print(userinput)
print(inputarray)
n = len(inputarray)
quickSort(inputarray, 0, n - 1)
print ("Sorted array is:")
for i in range(n):
    print("%d" % inputarray[i])