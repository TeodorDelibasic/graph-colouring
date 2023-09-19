from random_graph_generator import RandomGraphGenerator
from graph import Graph
from graph_colouring_algorithms.greedy_colouring_algorithm import GreedyColouringAlgorithm
from graph_colouring_algorithms.welsh_powell_colouring_algorithm import WelshPowellColouringAlgorithm
from my_error import MyError


def main():
    try:
        graph: Graph = RandomGraphGenerator.generate_for_edges(25)

        print(graph)

        graph.set_graph_colouring_algorithm(GreedyColouringAlgorithm())
        graph.colour()

        graph.set_graph_colouring_algorithm(WelshPowellColouringAlgorithm())
        graph.colour()
    except MyError as e:
        print(e)


if __name__ == "__main__":
    main()
