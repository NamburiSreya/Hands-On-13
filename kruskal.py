class Edge:
    def __init__(self, u, v, w):
        self.start = u
        self.end = v
        self.weight = w

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(vertices, edges):
    result = []
    i, e = 0, 0
    edges = sorted(edges, key=lambda item: item.weight)
    parent = []
    rank = []
    
    for node in range(vertices):
        parent.append(node)
        rank.append(0)
    
    while e < vertices - 1:
        edge = edges[i]
        i += 1
        x = find(parent, edge.start)
        y = find(parent, edge.end)
        
        if x != y:
            e += 1
            result.append(edge)
            union(parent, rank, x, y)
    
    return result

# Adjacency matrix
adjacency_matrix = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
num_vertices = len(vertices)

edges = []
for i in range(num_vertices):
    for j in range(i+1, num_vertices):
        if adjacency_matrix[i][j] != 0:
            edges.append(Edge(i, j, adjacency_matrix[i][j]))

mst = kruskal(num_vertices, edges)

print("Edges of Minimum Cost Spanning Tree are:")
for edge in mst:
    print(f"{vertices[edge.start]} -> {vertices[edge.end]} = {edge.weight}")

#output
#Edges of Minimum Cost Spanning Tree are:
#g -> h = 1
#c -> i = 2
#f -> g = 2
#a -> b = 4
#c -> f = 4
#c -> d = 7
#a -> h = 8
#d -> e = 9
