# def add_node(v):
#     global node_count
#     if v in node:
#         print("node is present in the node")
#     else:
#         node_count = node_count + 1
#         node.append(v)
#         for i in graph:
#             i.append(0)
#         temp = []
#         for i in range(node_count):
#             temp.append(0)
#         graph.append(temp)
#
#
# def add_edge(vert1, vert2):  # if you went to add weighted edge assign weight instead of 1
#     if vert1 not in node:
#         print(vert1, " is not present in the graph")
#     elif vert2 not in node:
#         print(vert2, " is not present in the graph")
#     else:
#         index1 = node.index(vert1)
#         index2 = node.index(vert2)
#         graph[index2][index1] = 1
#         graph[index1][index2] = 1
# def trav():
#
#     for i in range(node_count):
#         for j in range(node_count):
#             print(format(graph[i][j],"9"), end=" ")
#         print()

# The above code is work for adjacency matrix representation
# The given bellow code works for adjacency list representation of graph
def add_node(v):
    if v in graph:
        print("the node is already exist")
    else:
        graph[v]=[]

def add_edge(v1,v2,cost):# unweighted and undirected graph
    if v1 not in graph:
        print(v1," is not present in the graph")
    elif v2 not in graph:
        print(v2, " is not present in the graph")
    else:
        list1=[v2,cost]
        list2=[v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)





node = []
graph = {}
node_count = 0
add_node(4)
add_node(5)
add_edge(4,5,30)

print(graph)
