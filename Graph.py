def add_node(v):
    global node_count
    if v in node:
        print("node is present in the node")
    else:
        node_count = node_count + 1
        node.append(v)
        for i in graph:
            i.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)


def add_edge(vert1, vert2):  # if you went to add weighted edge assign weight instead of 1
    if vert1 not in node:
        print(vert1, " is not present in the graph")
    elif vert2 not in node:
        print(vert2, " is not present in the graph")
    else:
        index1 = node.index(vert1)
        index2 = node.index(vert2)
        graph[index2][index1] = 1
        graph[index1][index2] = 1

# The above code is work for adjacency matrix representation
# The given bellow code works for adjacency list representation of graph
def add_nodel(v):
    if v in graph:
        print("the node is already exist")
    else:
        graph[v]-[]

def add_edge(v1,v2):# unweighted and undirected graph
    if v1 not in graph:
        print(v1," is not present in the graph")
    elif v2 not in graph:
        print(v2, " is not present in the graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


def trav():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"9"), end=" ")
        print()


node = []
graph = []
node_count = 0
print("graph before adding")
print(graph)
add_node("r")
add_node(5)
add_node(90)
print("graph after adding the node")
trav()
print("before adding the edge")
add_edge("r", 5)
add_edge("r", 90)
add_edge(90, 5)
print("r 5 90")
trav()
