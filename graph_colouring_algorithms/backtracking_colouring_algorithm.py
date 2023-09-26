from graph_colouring_algorithms.abstract_colouring_algorithm import AbstractColouringAlgorithm


class BacktrackingColouringAlgorithm(AbstractColouringAlgorithm):

    def is_safe(self, graph, vertex, colour):
        for neighbour in graph.vertices[vertex][1]:
            if colour == graph.vertices[neighbour][0]:
                return False
        return True

    def colour_graph(self, graph):
        for number_of_colors in range(1, len(graph.vertices) + 1):
            if self.colour_graph_util(graph, 0, number_of_colors):
                return
            graph.reset_colors()

    def colour_graph_util(self, graph, index, n):
        if index == len(graph.vertices):
            return True

        vertex = list(graph.vertices.keys())[index]
        properties = graph.vertices[vertex]

        if properties[0] != -1:
            return self.colour_graph_util(graph, index + 1, n)

        for colour in range(n):
            if not self.is_safe(graph, vertex, colour):
                continue

            properties[0] = colour
            if self.colour_graph_util(graph, index + 1, n):
                return True
            properties[0] = -1

        return False

    def __str__(self):
        return "Backtracking Colouring Algorithm"
