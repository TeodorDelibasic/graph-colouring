import time
from my_error import MyError


class Graph:

    # { vertex_number: (color, adjacency_list) }
    def __init__(self):
        self.vertices = {}
        self.colouring_algorithm = None

    def add_vertex(self, vertex):
        if vertex in self.vertices:
            raise MyError("Vertex already exists.")
        self.vertices[vertex] = [-1, set()]

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            raise MyError("Vertices don't exist in the graph.")
        if vertex1 in self.vertices[vertex2][1] or vertex2 in self.vertices[vertex1][1]:
            raise MyError(f"Edge already exists. {vertex1} - {vertex2}")
        self.vertices[vertex1][1].add(vertex2)
        self.vertices[vertex2][1].add(vertex1)

    def vertex_exists(self, vertex):
        return vertex in self.vertices.keys()

    def edge_exists(self, vertex1, vertex2):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            raise MyError("Vertices don't exist in the graph.")
        return vertex2 in self.vertices[vertex1][1]

    def get_vertex_degree(self, vertex):
        return len(self.vertices[vertex][1])

    def get_vertex_saturation_degree(self, vertex):
        return len(set(self.vertices[neighbour][0]
                       for neighbour in self.vertices[vertex][1]
                       if self.vertices[neighbour][0] != -1))

    def set_graph_colouring_algorithm(self, colouring_algorithm):
        self.colouring_algorithm = colouring_algorithm

    def reset_colors(self):
        for v in self.vertices.values():
            v[0] = -1

    def check_colouring(self):
        for vertex, [vertex_colour, neighbours] in self.vertices.items():
            for neighbour in neighbours:
                if vertex_colour == self.vertices[neighbour][0]:
                    raise MyError(f"Same color for neighbours {vertex} and {neighbour}")

    def colour(self):
        self.reset_colors()

        start_time = time.perf_counter()
        self.colouring_algorithm.colour_graph(self)
        end_time = time.perf_counter()

        # print(f"Time taken: {end_time - start_time}")
        # print(f"Graph coloured with {self.colouring_algorithm}"
        #       f"using {self.get_number_of_colours()} colors.")
        # print("\n".join(f"{vertex} -> {colour}"
        #                 for vertex, [colour, _] in self.vertices.items()))

        self.check_colouring()

        return end_time - start_time

    def get_number_of_colours(self):
        return len({colour for colour, _ in self.vertices.values()})

    def __str__(self):
        return "\n".join(f"{vertex} ({props[0]}) -> {props[1]}" for vertex, props in self.vertices.items())
