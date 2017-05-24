import sys
import queue
import time
from collections import deque
from collections import defaultdict
# Declaration of Dictioary types: Default Dictionaries
data_dict = defaultdict(list)
# Declration of all the variables used
myworld=defaultdict(list)
visitedworld=defaultdict(list)
visited=0
notvisited=1
myqueue=[]
IDqueue=[]
result=[]
found=0
iteration=0
insource=''
indestination=''
ssource=''
distance=0
cost=0
filename=''
filecontent=''
startflag=1
currentdepth=0
exists=''
nodeflag=0

# The Start here method is called to read the file and get the input from the user for processing.

def starthere(self):
    print("Open and Print the Input File")
    # Reading the input file in a Dictionary myworld
    with open(filename, 'r') as Newfile:
        for line in Newfile.read().split("\n"):
            words=line.split(',')
            source=words[0]
            visitedworld[source]=visited
            destination=words[1]
            distance=words[2]
            detail=(destination,distance)
            myworld[source].append(detail)
    print(visitedworld)
    print('This is my world',myworld)
    size=len(myworld)
    print(size)
    userinput=str(self).split(',')
    insource=userinput[0]
    ssource=insource
    print(insource)
    indestination=userinput[1]
    inmethod=userinput[2]
    print(insource,indestination,inmethod)
    # The below section will et evaluated as per the inputs from the user
    # BFS: Method is Breadth first Search
    if (inmethod=='BFS'):
        print('Method is BFS.')
        startflag=0
        zeros=0
        print(myworld)
        for keys,values in myworld.items():
            if ssource==keys:
                startflag=1
                result.append([ssource,zeros])
                visitedworld[keys]=1
                if keys==indestination:
                    print('Final path from',insource,'to',indestination,'is:',result,'the path cost is:',cost)
                    startflag=0
                    res_str='Breadth first Search: Path from '+insource+' to '+indestination+' is: '+str(result)+' the cost of path travelled is: '+str(cost)
                    print("Result String is:",str(res_str))
                    writefile=open("result.txt","w")
                    writefile.write(res_str)
                    writefile.close()
        if startflag==1:
            bfs_search(ssource,indestination,myqueue,visitedworld)
            print('Final path from',insource,'to',indestination,'is:',result,'the cost of path travelled is:',cost)
            res_str='Breadth First Search: Path from '+insource+' to '+indestination+' is: '+str(result)+' the cost of path travelled is: '+str(cost)
            print("Result String is:",str(res_str))
            writefile=open("result.txt","w")
            writefile.write(res_str)
            writefile.close()
    # DFS: Method is Depth first Search
    elif (inmethod=='DFS'):
        print('Method is DFS.')
        startflag=0
        zeros=0
        found=0
        print(myworld)
        for keys,values in myworld.items():
            if ssource==keys:
                startflag=1
                result.append([ssource,zeros])
                visitedworld[keys]=1
                if keys==indestination:
                    print('Final path from',insource,'to',indestination,'is:',result,'the cost of path travelled is:',cost)
                    startflag=0
                    res_str='Depth First Search: Path from '+insource+' to '+indestination+' is: '+str(result)+' the cost of path travelled is: '+str(cost)
                    print("Result String is:",str(res_str))
                    writefile=open("result.txt","w")
                    writefile.write(res_str)
                    writefile.close()
        if startflag==1:
            retval = Dfs_search(ssource,indestination,myqueue,visitedworld)
            print('return valus is',retval)
            if retval==1:
                print('Final path from',insource,'to',indestination,'is:',result,'the cost of path travelled is:',cost)
                res_str='Depth First Search: Path from '+insource+' to '+indestination+' is: '+str(result)+' the cost of path travelled is: '+str(cost)
                print("Result String is:",str(res_str))
                writefile=open("result.txt","w")
                writefile.write(res_str)
                writefile.close()
            else:
                print("There is no path from source to destination")
    # ID: Method is Iterative Deepening Search
    elif (inmethod=='ID'):
        print('Method is Iterative Deepening.')
        print(myworld)
        startflag=0
        exists==False
        for incrementer in range(50):
            print('Implementing depth',incrementer)
            global cost,result
            startflag=0
            exists==False
            IDqueue=[]
            found=0
            nodeflag=0
            cost=0
            result=[]
            for keys in visitedworld:
                visitedworld[keys]=0
            if found==1:
                print('Destination found, Break')
                break
            if exists==True:
                print('All Nodes searched in ID:')
                exists==False
                break
            for keys,values in myworld.items():
                if ssource==keys:
                    startflag=1
                    zeros=0
                    IDqueue.append([keys,zeros])
                    result.append([keys,zeros])
                    print('new idqueue is:',IDqueue)
                    visitedworld[keys]=1
                    if keys==indestination:
                        startflag=0
                        print('Final path for interation depth=',incrementer,'from',insource,'to',indestination,'is:',IDqueue,'the cost of path travelled is:',cost)
                        res_str='Iterative Deepening: Path for iteration depth=',str(incrementer),'from',insource,'to',indestination,'is:',str(IDqueue),'the cost of path travelled is:',str(cost)
                        print("Result String is:",str(res_str))
                        writefile=open("result.txt","w")
                        writefile.write(res_str)
                        writefile.close()
            if (startflag==1 and currentdepth<incrementer):
                print('start ID operations')
                depth=incrementer
                D_search(ssource,indestination,IDqueue,visitedworld,depth,currentdepth,result,insource)
            elif(startflag==1 and currentdepth==incrementer):
                print('No result found at depth:',incrementer)
    else: print('Invalid Input Method.')

# Method to Traverse the node Depth wise
def Dfs_search(ssource,indestination,myqueue,visitedworld):
    global found,notvisited,cost
    print("Function Call",ssource)
    for values in myworld[ssource]:
        if found==0:
            if(visitedworld[values[0]]==0):
                myqueue.insert(0,[values[0],values[1]])
                visitedworld[values[0]]=notvisited
                cost=cost+int(values[1])
                print('my Queue is:', myqueue)
                print('value is:',values[0],values[1])
                print('dest is:',indestination)
                print('cost is:',cost)
                if values[0]==indestination:
                    found=1
                    for item in reversed(myqueue):
                        result.append([item[0],item[1]])
                else:
                    ssource=values[0]
                    # Recursive Function call for Depth search
                    Dfs_search(ssource,indestination,myqueue,visitedworld)
    return found





# Called by the bfs_search function: Pop the traversed element
def bfs(ssource,found,myqueue,indestination):
        if found==0:
            ssource=myqueue[0][0]
            myqueue.pop(0)
            print(myqueue,ssource)
            bfs_search(ssource,indestination,myqueue,visitedworld)
        if found==1:
            print('result found:', myqueue)
# Method to traverse all the first adjacent cities from the current city
def bfs_search(ssource,indestination,myqueue,visitedworld):
    global found,notvisited,cost
    print("Function Call",ssource)
    for values in myworld[ssource]:
        if(visitedworld[values[0]]==0):
            myqueue.append([values[0],values[1]])
            result.append([values[0],values[1]])
            print('lol',int(values[1]))
            cost=cost+int(values[1])
            visitedworld[values[0]]=notvisited
            print('my queue is:',myqueue)
            print('my index id:',indestination,',',values[0])
            print('distance travelled:',cost)
            if values[0]==indestination:
                found=1
                break
    print(ssource,myqueue[0][0],found)
    bfs(ssource,found,myqueue,indestination)

# Method to traverse the nodes Depth wise until reached the maximum depth
def D_search(ssource,indestination,IDqueue,visitedworld,depth,currentdepth,result,insource):
    global found,notvisited,cost,exists,nodeflag
    if found==0:
        if len(IDqueue)>0:
            nodeflag=0
            print("DSearch Function Call",ssource)
            for values in myworld[ssource]:
                if(visitedworld[values[0]]==0):
                    nodeflag=1
                    IDqueue.insert(0,[values[0],values[1]])
                    result.append([values[0],values[1]])
                    visitedworld[values[0]]=notvisited
                    cost=cost+int(values[1])
                    print('My queue is:',IDqueue)
                    print('Value is:',values[0],values[1])
                    print('Destination is:',indestination)
                    print('cost is:',cost)
                    if values[0]==indestination:
                        found=1
                        print('Destination found')
                        print('Final path for interation depth=',depth,'from',insource,'to',indestination,'is:',result,'the cost of path travelled is:',cost)
                        res_str='Iterative Deepening: Path for iteration depth= '+str(depth)+' from '+insource+' to '+indestination+' is: '+str(result)+' the cost of path travelled is: '+str(cost)
                        print("Result String is:",str(res_str))
                        writefile=open("result.txt","w")
                        writefile.write(res_str)
                        writefile.close()
                        sys.exit('Destination found: Program exit...')
                    currentdepth+=1
                    print('D-CD:',currentdepth)
                    print('D-de:',depth)
                    if currentdepth<depth:
                        ssource=values[0]
                        D_search(ssource,indestination,IDqueue,visitedworld,depth,currentdepth,result,insource)
                    if(currentdepth==depth and found==0):
                        b_search(ssource,indestination,IDqueue,visitedworld,depth,currentdepth,result,insource)
            if (nodeflag==0 and len(IDqueue)>0):
                b_search(ssource,indestination,IDqueue,visitedworld,depth,currentdepth,result,insource)
        else:
            print('No nodes left to discover in D')
            return
# Method to search the other child nodes of the current node.
def b_search(ssource,indestination,IDqueue,visitedworld,depth,currentdepth,result,insource):
    global found,notvisited,cost,exists,nodeflag
    if found==0:
        if len(IDqueue)>0:
            IDqueue.pop(0)
        print('IDQueue is:',IDqueue)
        print('Len of IDQueue:',len(IDqueue))
        if len(IDqueue)>0:
            nodeflag=0
            currentdepth-=1
            ssource=IDqueue[0][0]
            print("BSearch Function Call",ssource)
            print('B-CD:',currentdepth)
            print('B-de:',depth)
            exists=all(visitedworld[values[0]]==1 for values in myworld[ssource])
            print('exit flag value is:',exists)
            for values in myworld[ssource]:
                if exists==True:
                    print('All nodes searched at levelB:')
                    exists=False
                    break
                if(visitedworld[values[0]]==0):
                    nodeflag=1
                    IDqueue.insert(0,[values[0],values[1]])
                    result.append([values[0],values[1]])
                    print('cost',int(values[1]))
                    cost=cost+int(values[1])
                    visitedworld[values[0]]=notvisited
                    print('my queue is:',IDqueue)
                    print('my index id:',indestination,',',values[0])
                    print('distance travelled:',cost)
                    if values[0]==indestination:
                        found=1
                        print('Final path for interation depth=',depth,'from',insource,'to',indestination,'is:',result,'the cost of path travelled is:',cost)
                        res_str='Iterative Deepening: Path for iteration depth= '+str(depth)+' from '+insource+' to '+indestination+' is: '+str(result)+' the cost of path travelled is: '+str(cost)
                        print("Result String is:",str(res_str))
                        writefile=open("result.txt","w")
                        writefile.write(res_str)
                        writefile.close()
                        sys.exit('Destination found: Program exit...')
                    currentdepth+=1
                    print('After-CD:',currentdepth)
                    print('After-de:',depth)
                    if currentdepth<depth:
                        ssource=values[0]
                        D_search(ssource,indestination,IDqueue,visitedworld,depth,currentdepth,result,insource)
                    if(currentdepth==depth and found==0):
                        b_search(ssource,indestination,IDqueue,visitedworld,depth,currentdepth,result,insource)
            if (nodeflag==0 and len(IDqueue)>0):
                b_search(ssource,indestination,IDqueue,visitedworld,depth,currentdepth,result,insource)
        else:
            print('No nodes left to discover in B')
            return

# Program Execution starts here .....
print('To Begin processing please create/save the input Graph in csv format as a .txt file in the project directory...After completed please type OK(Uppercase): ')
Uerfile=input()
if (Uerfile=='OK'):
    print('Please enter the file name, attached in the previous step: ')
    filename=input()
    print('Please enter source,destination,search method: ')
    userinput=input()
    starthere(self=userinput)
else:
    print('Invalid user input...Please save the file first and then input ok...')
