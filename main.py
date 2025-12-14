import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Task 1: Create a graph to model a city's transportation network

# Create an undirected graph
G = nx.Graph()

# Add nodes (some metro stations in Kyiv)
stations = [
"Tarasa Shevchenka",
"Kontraktova Ploshcha",
"Poshtova Ploshcha",
"Maidan Nezalezhnosti",
"Plosha Lva Tolstoho",
"Olimpiiska",
"Palats Sportu",
"Politekhnichnyi Instytut",
"Vokzalna",
"Universytet",
"Teatralna",
"Khreshchatyk",
"Arsenalna",
"Dnipro",
"Lukianivska",
"Zoloti Vorota",
"Palats Sportu",
"Klovska",
]

G.add_nodes_from(stations)

# Add edges (connections between stations with distances in km)
connections = [
    # blue line
    ("Tarasa Shevchenka", "Kontraktova Ploshcha", 1),
    ("Kontraktova Ploshcha", "Poshtova Ploshcha", 0.5),
    ("Poshtova Ploshcha", "Maidan Nezalezhnosti", 1.2),
    ("Maidan Nezalezhnosti", "Plosha Lva Tolstoho", 0.8),
    ("Plosha Lva Tolstoho", "Olimpiiska", 1.0),
    # red line
    ("Politekhnichnyi Instytut", "Vokzalna", 1.5),
    ("Vokzalna", "Universytet", 1.3),
    ("Universytet", "Teatralna", 0.7),
    ("Teatralna", "Khreshchatyk", 0.4),
    ("Khreshchatyk", "Arsenalna", 1.1),
    ("Arsenalna", "Dnipro", 1.4),
    # green line
    ("Lukianivska", "Zoloti Vorota", 0.9),
    ("Zoloti Vorota", "Palats Sportu", 1.2),
    ("Palats Sportu", "Klovska", 1.6),
    # change lines connections
    ("Maidan Nezalezhnosti", "Khreshchatyk", 0.1),
    ("Plosha Lva Tolstoho", "Palats Sportu", 0.1),
    ("Zoloti Vorota", "Teatralna", 0.1),



]

# Add edges with weight attribute (distance)
for station1, station2, distance in connections:
    G.add_edge(station1, station2, weight=distance)

# Display basic information about the graph
print("=== City Transportation Network (Kyiv Metro) ===\n")
print(f"Number of stations (nodes): {G.number_of_nodes()}")
print(f"Number of connections (edges): {G.number_of_edges()}")
print(f"\nDegree of each station:")
for node, degree in sorted(G.degree(), key=lambda x: x[1], reverse=True):
    print(f"  {node}: {degree} connections")

# Visualize the graph
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

# Draw the network
nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                       node_size=800, alpha=0.9)
nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')
nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color='gray')

# Draw edge labels (distances)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=7)

plt.title("Kyiv Metro Transportation Network", fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()
plt.savefig('transportation_network.png', dpi=300, bbox_inches='tight')
print("\n✓ Graph visualization saved as 'transportation_network.png'")
plt.show()

print("\n" + "="*70)

# Task 2: Implement DFS and BFS to find paths in the graph

# Using NetworkX graph directly - G[node] gives adjacency list
# NetworkX graphs support dictionary-like access: G[node] returns neighbors

def dfs_recursive(graph, vertex, visited=None):
    """DFS algorithm - explores deeply before backtracking"""
    if visited is None:
        visited = set()
    
    visited.add(vertex)
    print(vertex, end=' ')  # Відвідуємо вершину
    
    for neighbor in sorted(graph[vertex]):  # graph[vertex] returns neighbors
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    
    return visited

def bfs_recursive(graph, queue, visited=None):
    """BFS algorithm - explores level by level"""
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return visited
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Якщо не відвідували, друкуємо вершину
        print(vertex, end=" ")
        # Додаємо вершину до множини відвіданих вершин.
        visited.add(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        # graph[vertex] returns neighbors (adjacency list)
        queue.extend(sorted(set(graph[vertex]) - visited))
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    return bfs_recursive(graph, queue, visited)

# Test both algorithms starting from the same station
start_station = "Maidan Nezalezhnosti"

print("\n=== Task 2: Path Finding with DFS and BFS ===\n")

# DFS traversal
print(f"DFS (Depth-First Search) starting from '{start_station}':")
print("Path: ", end="")
dfs_visited = dfs_recursive(G, start_station)
print(f"\nTotal stations visited: {len(dfs_visited)}")

print("\n" + "-"*70 + "\n")

# BFS traversal
print(f"BFS (Breadth-First Search) starting from '{start_station}':")
print("Path: ", end="")
bfs_visited = bfs_recursive(G, deque([start_station]))
print(f"\nTotal stations visited: {len(bfs_visited)}")
