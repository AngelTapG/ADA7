def warshall(graph):
    V = len(graph)
    
    reach = [[graph[i][j] for j in range(V)] for i in range(V)]

    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if reach[i][k] and reach[k][j]:
                    reach[i][j] = 1

    
    print_solution(reach)

def print_solution(reach):
    print("La matriz de cerradura transitiva es:")
    for row in reach:
        print(" ".join(str(int(val)) for val in row))


graph = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

warshall(graph)