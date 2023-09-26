from graph_colouring_algorithms.abstract_colouring_algorithm import AbstractColouringAlgorithm


class GreedyColouringAlgorithm(AbstractColouringAlgorithm):

    def colour_graph(self, graph):
        colours = set()
        for vertex_properties in graph.vertices.values():
            available_colours = colours.copy()
            for adjacent in vertex_properties[1]:
                if graph.vertices[adjacent][0] in available_colours:
                    available_colours.remove(graph.vertices[adjacent][0])
            vertex_properties[0] = available_colours.pop() \
                if len(available_colours) > 0 \
                else len(colours)
            colours.add(vertex_properties[0])

    def __str__(self):
        return "Greedy Colouring Algorithm"
