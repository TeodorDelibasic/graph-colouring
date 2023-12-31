from graph_colouring_algorithms.abstract_colouring_algorithm import AbstractColouringAlgorithm
import heapq


class DSaturColouringAlgorithm(AbstractColouringAlgorithm):

    def colour_graph(self, graph):
        pq = [(0, -graph.get_vertex_degree(v), v) for v in graph.vertices.keys()]
        heapq.heapify(pq)

        while pq:
            _, _, vertex = heapq.heappop(pq)

            if graph.vertices[vertex][0] != -1:
                continue

            used_colours = {graph.vertices[neighbour][0]
                            for neighbour in graph.vertices[vertex][1]
                            if graph.vertices[neighbour][0] != -1}

            for colour in range(len(graph.vertices)):
                if colour not in used_colours:
                    graph.vertices[vertex][0] = colour

            for neighbour in graph.vertices[vertex][1]:
                if graph.vertices[neighbour][0] != -1:
                    heapq.heappush(pq, (-graph.get_vertex_saturation_degree(neighbour),
                                        -graph.get_vertex_degree(neighbour),
                                        neighbour))

    def __str__(self):
        return "DSatur Colouring Algorithm"
