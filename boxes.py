import sys
from collections import defaultdict
#dont do networkx or numpy!!!

#take input from CL
inFile = sys.argv[1]
input = open(inFile,'r').read().splitlines()

## Get 1st line
numBoxes = int(input[0])
print('Number of Boxes:', numBoxes)
#get boxes into correct format (list of lists of ints)
boxes = input[1:]
print("List of sorted dimensions:")
dims = []
for i in range(numBoxes):
    dims.append([int(j) for j in boxes[i].split(' ')])
    dims[i].sort()
print(dims)

#building the graph: 
# start with source -> left, right -> term, eg:
#   l1  r1
# s l2  r2  t
#   l3  r3
# then want a matching function that returns 1 if a box fits inside another and 0 o.w.
# connect left to right for boxes which nest
# then run FF, ???, profit
# could you just use the size of the matching?

# want something like:
# dict {    
#           "s" : ["L1", ..., "Ln"],
#           "R1" : ["t"],
#           ...,
#           "Rn" : ["t"]
#       } or could you just do t like you do s (does cardinality matter?)

class Graph:
    def __init__(graph):
        graph.dict = defaultdict(list)

    def add(graph,node,adjacent_node): 
        graph.dict[node].append(adjacent_node)

G = Graph()

for i in range(numBoxes):
    G.add('S', f'L{i}') #left side of bipartite S -> L
    G.add(f'R{i}', 'T') #right side of bipartite R -> T

print('Graph:', G.dict)

# calculate matching boxes and add to graph

def match(list, i, j): # returns 1 if box i nests in box j
    # sorted box dimensions makes this easy
    if ((list[j][0] - list[i][0]) > 0) and ((list[j][1] - list[i][1]) > 0) and ((list[j][2] - list[i][2]) > 0):
        return 1
    else:
        return 0

#loop to find matches

for i in range(numBoxes):
    for j in range(numBoxes):
        if(i!=j):
            if (match(dims, i, j) == 1): 
                G.add(f'L{i}', f'R{j}')
                print('Matching pair:', i, j)

print('Matched Graph:', G.dict)

