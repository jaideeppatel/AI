# Heap Sort

def heapify(inputarray, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
    print("before largest l r n", largest,l,r,n)
    # See if left child of root exists and is
    # greater than root
    if l < n and inputarray[i] < inputarray[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and inputarray[largest] < inputarray[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        inputarray[i], inputarray[largest] = inputarray[largest], inputarray[i]  # swap
        print("after largest l r n", largest,l,r,n)
        # Heapify the root.
        heapify(inputarray, n, largest)

# The main function to sort an array of given size
def heapSort(inputarray):
    n = len(inputarray)

    # Build a maxheap.
    for i in range(int(n/2), -1, -1): ## Start processing to get the max heap from non leaf nodes
        print("I value is:",i)
        heapify(inputarray, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        inputarray[i], inputarray[0] = inputarray[0], inputarray[i]   # swap
        heapify(inputarray, i, 0)

# Program Execution starts here .....
print('Enter the Input array')
userinput=input()
inputarray=[]
for items in userinput.split(' '):
    inputarray.append(int(items))
print(userinput)
print(inputarray)
heapSort(inputarray)
n = len(inputarray)
print ("Sorted array is")
for i in range(n):
    print ("%d" % inputarray[i])