from graph import Graph
from collections import OrderedDict

grafo = Graph(False)
grafo.load("./../tests/ciclo_euleriano/ContemCicloEuleriano.net")
# grafo.render()

print("BFS")
grafo.searchBFS(0)

# Eulerian Cicle
print("\nHierholzer")
(result, cicle) = grafo.detect_eulerian_cicle()
print(int(result))
print(grafo.vertices_to_index(cicle))

# Dijkstra 
grafo = Graph(False)
grafo.load("./../tests/caminho_minimo/fln_pequena.net")
print("\nDijkstra")
start_node = grafo.getVertice(0)
(previous_nodes, shortest_path) = grafo.dijikstra(start_node)
for i in range(grafo.qtdVertices()):
    grafo.print_dijikstra(previous_nodes, shortest_path, start_node, grafo.getVertice(i))


floyd = grafo.floydWarshall()

print('Floyd Warshall:')
for key, value in floyd.items():
    distances = ""
    sort_orders = sorted(value.items(), key=lambda x: x[1], reverse=False)
    for i in sort_orders:
        distances += str(grafo.vertice_to_index(i[0])) + ","
    print(grafo.vertice_to_index(key), ":", distances[:-1])

manha = Graph(False)
manha.load("./../tests/dirigidos/manha.net")
manha.render()
