def perform_dfs(current_node, graph, visited, node_labels):
    """
    Perform Depth-First Search starting from the current node.
    
    Args:
    current_node (int): Index of the current node.
    graph (list): Adjacency matrix representing the graph.
    visited (list): List to keep track of visited nodes.
    node_labels (list): List of node names/labels.
    """
    print(node_labels[current_node], end=" ")
    visited[current_node] = True

    for neighbor in range(len(graph)):
        if not visited[neighbor] and graph[current_node][neighbor] == 1:
            perform_dfs(neighbor, graph, visited, node_labels)

def main():
    # Number of nodes in the graph
    NUM_NODES = 9
    
    # Adjacency matrix representation of the graph
    graph = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # watch
        [0, 0, 1, 1, 0, 0, 0, 0, 0],  # shirt
        [0, 0, 0, 0, 0, 0, 0, 0, 1],  # tie
        [0, 0, 0, 0, 0, 0, 0, 0, 1],  # belt
        [0, 0, 0, 1, 0, 0, 0, 0, 0],  # pants
        [0, 0, 0, 0, 1, 0, 0, 1, 0],  # undershorts
        [0, 0, 0, 0, 0, 0, 0, 1, 0],  # socks
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # shoes
        [0, 0, 0, 0, 0, 0, 0, 0, 0]   # jacket
    ]

    # Initialize all nodes as not visited
    visited = [False] * NUM_NODES
  
    # Labels for each node
    node_labels = ["watch", "shirt", "tie", "belt", "pants", "undershorts", "socks", "shoes", "jacket"]

    print("DFS traversal of the graph:")
 
    # Perform DFS for each unvisited node
    for node in range(NUM_NODES):
        if not visited[node]:
            perform_dfs(node, graph, visited, node_labels)

if __name__ == "__main__":
    main()

#output
#DFS traversal of the graph:
#watch shirt tie jacket belt pants undershorts shoes socks 