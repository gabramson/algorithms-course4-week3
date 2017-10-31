import numpy as np

class TSPFinder:
    def __init__(self, num_edges):
        self.num_edges = num_edges
        self.edges = np.empty([num_edges, 2], dtype=float)
        self.unvisited = set()

    def add_edge(self, edge_id, lat, lon):
        self.edges[edge_id-1][0]=lat
        self.edges[edge_id-1][1]=lon
        self.unvisited.add(edge_id)

    def get_shortest_tour(self):
        return 15