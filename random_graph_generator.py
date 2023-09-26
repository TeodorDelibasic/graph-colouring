from random import randint, random
from math import sqrt, ceil
from graph import Graph


class RandomGraphGenerator:

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
