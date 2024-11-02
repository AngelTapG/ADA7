import heapq

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def agregar_arista(self, origen, destino, peso):
        self.adj_list[origen].append((destino, peso))
        self.adj_list[destino].append((origen, peso))  

    def dijkstra(self, origen):
        distancias = [float('inf')] * self.vertices
        distancias[origen] = 0
        pq = [(0, origen)]  
        
        while pq:
            distancia_actual, nodo_actual = heapq.heappop(pq)
            
            if distancia_actual > distancias[nodo_actual]:
                continue
            
            for vecino, peso in self.adj_list[nodo_actual]:
                distancia = distancia_actual + peso
                
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(pq, (distancia, vecino))

        self.mostrar_distancias(distancias, origen)

    def mostrar_distancias(self, distancias, origen):
        print(f"Distancias desde el nodo {origen}:")
        for i, distancia in enumerate(distancias):
            print(f"Hasta el nodo {i} es: {distancia}")


if __name__ == "__main__":
    vertices = int(input("Introduce el número de nodos: "))
    grafo = Grafo(vertices)
    
    num_aristas = int(input("Introduce el número de aristas: "))
    print("Introduce las aristas en el formato: origen destino peso")
    for _ in range(num_aristas):
        origen = int(input("Origen: "))
        destino = int(input("Destino: "))
        peso = int(input("Peso: "))
        grafo.agregar_arista(origen, destino, peso)
    
    nodo_origen = int(input("Introduce el nodo de origen para calcular distancias: "))
    grafo.dijkstra(nodo_origen)