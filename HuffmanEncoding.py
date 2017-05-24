from heapq import heappush, heappop, heapify
from collections import defaultdict

def encode(symb2freq):
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    print("-----before heapify",heap)
    heapify(heap)
    print("-----After heapify",heap)
    #print('Heap is:',heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        print('--------------------------------')
        print("lo -",lo , "hi -",hi)
        for pair in lo[1:]:
            print('lower pair',pair)
            pair[1] = '0' + pair[1]
            print('-----p1',pair[1])
        for pair in hi[1:]:
            print('higher pair',pair)
            pair[1] = '1' + pair[1]
            print('-----p1',pair[1])
        print('--------------------------------')
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

#txt = "this is an example for huffman encoding"
#symb2freq = defaultdict()
symb2freq = {'a':5,'b':13,'c':12,'d':16,'e':9,'f':45}
#!for ch in txt:
#    symb2freq[ch] += 1
# in Python 3.1+:
# symb2freq = collections.Counter(txt)
huff = encode(symb2freq)
print ("Symbol\tWeight\tHuffman Code")
for p in huff:
    print ("%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1]))