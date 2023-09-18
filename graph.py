from my_error import MyError


class Graph:

    # { vertex_number: [color, adjacency_list] }
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex in self.vertices:
            raise MyError("Vertex already exists.")
        self.vertices[vertex] = [-1, set()]

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            raise MyError("Vertices don't exist in the graph.")
        if vertex1 in self.vertices[vertex2][1] or vertex2 in self.vertices[vertex1][1]:
            raise MyError("Edge already exists.")
        self.vertices[vertex1][1].add(vertex2)
        self.vertices[vertex2][1].add(vertex1)

    def vertex_exists(self, vertex):
        return vertex in self.vertices.keys()

    def edge_exists(self, vertex1, vertex2):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            raise MyError("Vertices don't exist in the graph.")
        return vertex2 in self.vertices[vertex1][1]

    def reset_colors(self):
        for v in self.vertices.values():
            v[0] = -1

    def __str__(self):
        return "\n".join(f"{k} ({v[0]}) -> {v[1]}" for k, v in self.vertices.items())
