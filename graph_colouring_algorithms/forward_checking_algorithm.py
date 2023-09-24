from graph_colouring_algorithms.abstract_colouring_algorithm import AbstractColouringAlgorithm


class ForwardCheckingAlgorithm(AbstractColouringAlgorithm):

    def is_safe(self, graph, vertex, colour, available_colours):
        for neighbour in graph.vertices[vertex][1]:
            if colour == graph.vertices[neighbour][0]:
                return False
            if colour in available_colours[neighbour] and len(available_colours[neighbour]) == 1:
                return False
        return True

    def colour_graph(self, graph):
        for number_of_colors in range(1, len(graph.vertices) + 1):
            available_colours = {vertex: set(range(number_of_colors)) for vertex in graph.vertices}
            if self.colour_graph_util(graph, 0, number_of_colors, available_colours):
                return
            graph.reset_colors()

    def colour_graph_util(self, graph, index, n, available_colours):
        if index == len(graph.vertices):
            return True

        vertex = min([v for v in available_colours.keys() if graph.vertices[v][0] == -1],
                     key=lambda v: (len(available_colours[v]),
                                    -sum(1 for x in graph.vertices[v][1] if graph.vertices[x][0] == -1)))

        properties = graph.vertices[vertex]

        if index == len(graph.vertices) - 1 and len(available_colours[vertex]) == 1:
            properties[0] = available_colours[vertex].pop()
            return True

        ordered_colours = sorted([colour for colour in available_colours[vertex]],
                                 key=lambda c: sum(1 for x in graph.vertices[vertex][1]
                                                   if graph.vertices[x][0] == -1 and c in graph.vertices[x][1]))

        for colour in ordered_colours:
            if colour not in available_colours[vertex] or not self.is_safe(graph, vertex, colour, available_colours):
                continue

            properties[0] = colour

            orig_available_colours = {}
            for neighbour in graph.vertices[vertex][1]:
                orig_available_colours[neighbour] = available_colours[neighbour].copy()
                if colour in available_colours[neighbour]:
                    available_colours[neighbour].remove(colour)

            if self.colour_graph_util(graph, index + 1, n, available_colours):
                return True

            properties[0] = -1
            for neighbour in graph.vertices[vertex][1]:
                available_colours[neighbour] = orig_available_colours[neighbour]

        return False

    def __str__(self):
        return "Backtracking Colouring Algorithm with Forward Checking"
