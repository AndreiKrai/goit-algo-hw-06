=== Task 2: Path Finding with DFS and BFS ===

DFS (Depth-First Search) starting from 'Maidan Nezalezhnosti':
Path: Maidan Nezalezhnosti Khreshchatyk Arsenalna Dnipro Teatralna Universytet Vokzalna Politekhnichnyi Instytut Zoloti Vorota Lukianivska Palats Sportu Klovska Plosha Lva Tolstoho Olimpiiska Poshtova Ploshcha Kontraktova Ploshcha Tarasa Shevchenka 
Total stations visited: 17

----------------------------------------------------------------------

BFS (Breadth-First Search) starting from 'Maidan Nezalezhnosti':
Path: Maidan Nezalezhnosti Khreshchatyk Plosha Lva Tolstoho Poshtova Ploshcha Arsenalna Teatralna Olimpiiska Palats Sportu Kontraktova Ploshcha Dnipro Universytet Zoloti Vorota Klovska Tarasa Shevchenka Vokzalna Lukianivska Politekhnichnyi Instytut 
Total stations visited: 17

======================================================================

=== Comparison and Analysis ===
DIFFERENCE IN PATHS:

1. DFS (Depth-First Search):
   - Explores as FAR as possible along each branch before backtracking
   - Goes deep into one direction first
   - Visits stations in a 'depth-oriented' manner

2. BFS (Breadth-First Search):
   - Explores all neighbors at the CURRENT depth before moving deeper
   - Explores level by level (layer by layer)
   - Visits all immediate neighbors before going further

WHY THE PATHS ARE DIFFERENT:

DFS Strategy:
  • Uses a stack (recursion) - Last In, First Out (LIFO)
  • Picks a neighbor and immediately explores its neighbors
  • Only backtracks when it reaches a dead end or visited station
  • Result: Creates 'long chains' going deep into the graph

BFS Strategy:
  • Uses a queue - First In, First Out (FIFO)
  • Visits ALL immediate neighbors before going to next level
  • Explores in 'waves' expanding outward from the start
  • Result: Visits stations layer by layer from the starting point

PRACTICAL IMPLICATIONS:
  • BFS finds the SHORTEST path (minimum number of stations)
  • DFS might find a longer path but uses less memory
  • BFS is better for 'closest station' queries
  • DFS is better for 'explore all possibilities' scenarios