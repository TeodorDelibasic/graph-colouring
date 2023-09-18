from random_graph_generator import RandomGraphGenerator
from graph import Graph
from graph_colouring_algorithms.greedy_colouring_algorithm import GreedyColouringAlgorithm


def main():
    graph: Graph = RandomGraphGenerator.generate_for_edges(10)
    print(graph)
    graph.set_graph_colouring_algorithm(GreedyColouringAlgorithm())
    graph.colour()


if __name__ == "__main__":
    main()
