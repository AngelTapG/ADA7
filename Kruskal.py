class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u]) 
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(vertices, edges):
    
    edges.sort(key=lambda x: x[2])  
    uf = UnionFind(vertices)
    
    mst = []  
    total_cost = 0

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v): 
            uf.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost


vertices = 4  
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst, total_cost = kruskal(vertices, edges)
print("Aristas en el árbol de expansión mínima:")
for u, v, weight in mst:
    print(f"{u} - {v}: {weight}")

print(f"Costo total del árbol de expansión mínima: {total_cost}")