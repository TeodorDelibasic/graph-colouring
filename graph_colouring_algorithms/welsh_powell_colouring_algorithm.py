from graph_colouring_algorithms.abstract_colouring_algorithm import AbstractColouringAlgorithm


class WelshPowellColouringAlgorithm(AbstractColouringAlgorithm):

    def colour_graph(self, graph):
        colour = 0
        sorted_by_degree = sorted([vertex for vertex in graph.vertices.keys()],
                                  key=lambda x: graph.get_vertex_degree(x),
                                  reverse=True)

        for i in range(len(sorted_by_degree)):
            properties = graph.vertices[sorted_by_degree[i]]
            if properties[0] == -1:
                properties[0] = colour
                adjacent = properties[1].copy()
                for j in range(i + 1, len(sorted_by_degree)):
                    if graph.vertices[sorted_by_degree[j]][0] == -1 and \
                            sorted_by_degree[j] not in adjacent:
                        graph.vertices[sorted_by_degree[j]][0] = colour
                        adjacent = adjacent.union(graph.vertices[sorted_by_degree[j]][1])
                colour += 1

    def __str__(self):
        return "Welsh-Powell Colouring Algorithm"
