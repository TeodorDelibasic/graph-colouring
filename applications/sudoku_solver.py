from graph_colouring_algorithms.backtracking_colouring_algorithm import BacktrackingColouringAlgorithm
from graph import Graph
from my_error import MyError
import time


class SudokuSolver:

    def __init__(self, file_name):
        self.graph = None

        self.create_graph()
        self.load_initial_state(file_name)
        self.check_initial_state()

    def create_graph(self):
        self.graph = Graph()

        for i in range(9 * 9):
            self.graph.add_vertex(i)

        for row in range(9):
            for col in range(9):
                vertex = row * 9 + col

                for i in range(9):
                    if col != i:
                        try:
                            self.graph.add_edge(vertex, row * 9 + i)
                        except MyError:
                            pass

                for j in range(9):
                    if row != j:
                        try:
                            self.graph.add_edge(vertex, j * 9 + col)
                        except MyError:
                            pass

                box_row = row // 3
                box_col = col // 3
                for i in range(box_row * 3, (box_row + 1) * 3):
                    for j in range(box_col * 3, (box_col + 1) * 3):
                        if i != row or j != col:
                            try:
                                self.graph.add_edge(vertex, i * 9 + j)
                            except MyError:
                                pass

    def load_initial_state(self, file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if len(lines) != 9:
                raise MyError("File must contain exactly 9 lines.")

            for i, line in enumerate(lines):
                row = line.strip().split()
                if len(row) != 9:
                    raise MyError(f"Error on line {i + 1}")

                for j, num in enumerate(row):
                    if not num.isdigit() or not (0 <= int(num) <= 9):
                        raise MyError(f"Error on line {i + 1}, position {j + 1}")

                    if num != 0:
                        self.graph.vertices[i * 9 + j][0] = int(num) - 1

    def check_initial_state(self):
        for vertex, [vertex_colour, neighbours] in self.graph.vertices.items():
            for neighbour in neighbours:
                if self.graph.vertices[neighbour][0] != -1 and \
                        vertex_colour != -1 and \
                        self.graph.vertices[neighbour][0] == vertex_colour:
                    raise MyError(f"Invalid initial state: boxes"
                                  f"[{vertex // 9}][{vertex % 9}]"
                                  f"and"
                                  f"[{neighbour // 9}][{neighbour % 9}]")

    def solve(self):
        algorithm = BacktrackingColouringAlgorithm()

        start_time = time.perf_counter()
        if not algorithm.colour_graph_util(self.graph, 0, 9):
            raise MyError(f"Your Sudoku puzzle is not solvable.")
        end_time = time.perf_counter()

        self.graph.check_colouring()

        print(f"Sudoku solved after {round(end_time - start_time, 2)} seconds")

        for row in range(9):
            if row % 3 == 0 and row > 0:
                print("-" * 21)
            for col in range(9):
                if col % 3 == 0 and col > 0:
                    print("|", end=" ")
                print(self.graph.vertices[row * 9 + col][0] + 1, end=" ")
            print()
