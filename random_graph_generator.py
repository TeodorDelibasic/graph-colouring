from random import randint, random
from math import sqrt, ceil
from graph import Graph


class RandomGraphGenerator:
    @staticmethod
    def generate_for_edges(number_of_edges):
        min_vertices = ceil(0.5 + sqrt(0.25 + 2 * number_of_edges))
        max_vertices = 2 * number_of_edges

        graph = Graph()

        for i in range(number_of_edges):
            while True:
                vertex1, vertex2 = -1, -1
                while vertex1 == vertex2:
                    vertex1, vertex2 = randint(min_vertices, max_vertices), randint(min_vertices, max_vertices)

                if not graph.vertex_exists(vertex1):
                    graph.add_vertex(vertex1)
                if not graph.vertex_exists(vertex2):
                    graph.add_vertex(vertex2)
                if not graph.edge_exists(vertex1, vertex2):
                    graph.add_edge(vertex1, vertex2)
                    break

        return graph

    @staticmethod
    def generate_for_vertices(number_of_vertices, probability=0.5):
        graph = Graph()
        for i in range(number_of_vertices):
            graph.add_vertex(i)
        for i in range(number_of_vertices):
            for j in range(i + 1, number_of_vertices):
                if random() < probability:
                    graph.add_edge(i, j)
        return graph
