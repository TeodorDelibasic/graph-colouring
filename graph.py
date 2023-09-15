from my_error import MyError


class Graph:

    # { vertex_number: [color, adjacency_list] }
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex in self.vertices:
            raise MyError("Vertex already exists.")
        self.vertices[vertex] = [None, set()]

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            raise MyError("Vertices don't exist in the graph.")
        if vertex1 in self.vertices[vertex2][1] or vertex2 in self.vertices[vertex1][1]:
            raise MyError("Edge already exists.")
        self.vertices[vertex1][1].insert(vertex2)
        self.vertices[vertex2][1].insert(vertex1)
