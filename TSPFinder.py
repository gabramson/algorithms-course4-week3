import math
import numpy as np

class TSPFinder:
    def __init__(self, num_edges):
        self.num_edges = num_edges
        self.edges = np.empty([num_edges, 2], dtype=float)
        self.unvisited = set()

    def add_edge(self, edge_id, lat, lon):
        self.edges[edge_id-1][0] = lat
        self.edges[edge_id-1][1] = lon
        self.unvisited.add(edge_id)

    def get_shortest_tour(self):
        current = 1
        unvisited = self.unvisited
        unvisited.remove(1)
        total_distance = 0
        while len(unvisited) > 0:
            min_distance = float("inf")
            for try_edge in unvisited:
                try_distance = self.__get_distance(current, try_edge)
                if try_distance < min_distance:
                    best_edge = try_edge
                    min_distance = try_distance
                elif try_distance == min_distance and try_edge < best_edge:
                    best_edge = try_edge
                    min_distance = try_distance
            total_distance += math.sqrt(min_distance)
            unvisited.remove(best_edge)
            current = best_edge
        total_distance += math.sqrt(self.__get_distance(current, 1))
        return total_distance

    def __get_distance(self, head, tail):
        x_diff = self.edges[head-1][0] - self.edges[tail-1][0]
        y_diff = self.edges[head-1][1] - self.edges[tail-1][1]
        return math.pow(x_diff, 2) + math.pow(y_diff, 2)
