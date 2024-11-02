
INF = float('inf')

def floyd_warshall(graph):
    V = len(graph)
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]

    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    
    print_solution(dist)

def print_solution(dist):
    print("La matriz de distancias mínimas entre cada par de nodos es:")
    for i in range(len(dist)):
        for j in range(len(dist)):
            if dist[i][j] == INF:
                print("INF", end=" ")
            else:
                print(f"{dist[i][j]:3}", end=" ")
        print()


graph = [
    [0, 3, INF, 5],
    [2, 0, INF, 4],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0]
]

floyd_warshall(graph)