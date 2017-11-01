import math
import numpy as np

class TSPFinder:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = np.empty([num_vertices, 2], dtype=float)
        self.unvisited = set()

    def add_vertex(self, vertex_id, lat, lon):
        self.vertices[vertex_id-1][0] = lat
        self.vertices[vertex_id-1][1] = lon
        self.unvisited.add(vertex_id)

    def get_shortest_tour(self):
        current = 1
        unvisited = self.unvisited
        unvisited.remove(1)
        total_distance = 0
        while len(unvisited) > 0:
            unvisited_count = len(unvisited)
            if unvisited_count % 100 == 0:
                print (unvisited_count)
            min_distance = float("inf")
            for try_vertex in unvisited:
                try_distance = self.__get_distance(current, try_vertex)
                if try_distance < min_distance:
                    best_vertex = try_vertex
                    min_distance = try_distance
                elif try_distance == min_distance and try_vertex < best_vertex:
                    best_vertex = try_vertex
                    min_distance = try_distance
            total_distance += math.sqrt(min_distance)
            unvisited.remove(best_vertex)
            current = best_vertex
        total_distance += math.sqrt(self.__get_distance(current, 1))
        return total_distance

    def __get_distance(self, head, tail):
        x_diff = self.vertices[head-1][0] - self.vertices[tail-1][0]
        y_diff = self.vertices[head-1][1] - self.vertices[tail-1][1]
        return math.pow(x_diff, 2) + math.pow(y_diff, 2)
