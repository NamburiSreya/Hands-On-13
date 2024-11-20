Algorithms Implemented

1. Depth-First Search (DFS)
Explores as far as possible along each branch before backtracking
Traverses graph nodes systematically
Uses adjacency matrix representation

Handles disconnected graphs by checking unvisited nodes
2. Kruskal's Minimum Spanning Tree (MST)
Finds minimum cost spanning tree in a weighted graph
Uses greedy algorithm approach
Connects all vertices with minimum total edge weight
Prevents cycle formation during tree construction

3. Topological Sort
Orders vertices in a directed acyclic graph (DAG)
Respects dependencies between nodes
Useful for scheduling and task ordering
Handles complex dependency relationships

Requirements
Python 3.7+
No external libraries required

How to Run
Ensure Python is installed
Clone the repository
Run individual algorithm files directly

Algorithm Complexity
DFS
Time Complexity: O(V + E)
Space Complexity: O(V)

Kruskal's MST
Time Complexity: O(E log E)
Space Complexity: O(V + E)

Topological Sort
Time Complexity: O(N log N)
Space Complexity: O(N)

Limitations
Works with small to medium-sized graphs
Assumes well-formed input graphs
May require modifications for specific use cases

Potential Improvements
Add error handling
Implement more graph representations
Create generic graph traversal methods
Add visualization capabilities