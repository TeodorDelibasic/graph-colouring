from random_graph_generator import RandomGraphGenerator
from graph import Graph


def main():
    graph: Graph = RandomGraphGenerator.generate_for_edges(10)
    print(graph)


if __name__ == "__main__":
    main()
