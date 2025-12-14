import networkx as nx

# Task 3: Dijkstra's Algorithm - Shortest paths between all vertices

# Recreate the graph from main.py
G = nx.Graph()

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
    "Klovska",
]

G.add_nodes_from(stations)

connections = [
    ("Tarasa Shevchenka", "Kontraktova Ploshcha", 1),
    ("Kontraktova Ploshcha", "Poshtova Ploshcha", 0.5),
    ("Poshtova Ploshcha", "Maidan Nezalezhnosti", 1.2),
    ("Maidan Nezalezhnosti", "Plosha Lva Tolstoho", 0.8),
    ("Plosha Lva Tolstoho", "Olimpiiska", 1.0),
    ("Politekhnichnyi Instytut", "Vokzalna", 1.5),
    ("Vokzalna", "Universytet", 1.3),
    ("Universytet", "Teatralna", 0.7),
    ("Teatralna", "Khreshchatyk", 0.4),
    ("Khreshchatyk", "Arsenalna", 1.1),
    ("Arsenalna", "Dnipro", 1.4),
    ("Lukianivska", "Zoloti Vorota", 0.9),
    ("Zoloti Vorota", "Palats Sportu", 1.2),
    ("Palats Sportu", "Klovska", 1.6),
    ("Maidan Nezalezhnosti", "Khreshchatyk", 0.1),
    ("Plosha Lva Tolstoho", "Palats Sportu", 0.1),
    ("Zoloti Vorota", "Teatralna", 0.1),
]

for station1, station2, distance in connections:
    G.add_edge(station1, station2, weight=distance)


def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances


# Convert NetworkX graph to dictionary format
graph = {}
for node in G.nodes():
    graph[node] = {}
    for neighbor in G.neighbors(node):
        graph[node][neighbor] = G[node][neighbor]['weight']

# Find shortest paths between all vertices
print("Shortest paths between all graph vertices:\n")

for start_vertex in graph:
    distances = dijkstra(graph, start_vertex)
    print(f"{start_vertex}:")
    print(distances)
    print()
