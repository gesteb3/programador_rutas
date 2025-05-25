import networkx as nx

class Paquete:
    def __init__(self, destino, lat, lon):
        self.destino = destino
        self.lat = lat
        self.lon = lon

class Mapa:
    def __init__(self):
        self.grafo = nx.DiGraph()
        self.posiciones = {}

    def agregar_nodo(self, nombre, lat, lon):
        self.grafo.add_node(nombre)
        self.posiciones[nombre] = (lat, lon)

    def agregar_arista(self, origen, destino, peso):
        self.grafo.add_edge(origen, destino, weight=peso)

    def calcular_ruta(self, origen, destino):
        ruta = nx.dijkstra_path(self.grafo, origen, destino, weight='weight')
        costo = nx.dijkstra_path_length(self.grafo, origen, destino, weight='weight')
        return ruta, costo
