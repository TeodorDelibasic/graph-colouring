from random_graph_generator import RandomGraphGenerator
from graph import Graph
from graph_colouring_algorithms.greedy_colouring_algorithm import GreedyColouringAlgorithm
from graph_colouring_algorithms.welsh_powell_colouring_algorithm import WelshPowellColouringAlgorithm
from graph_colouring_algorithms.degree_of_saturation_algorithm import DSaturColouringAlgorithm
from graph_colouring_algorithms.backtracking_colouring_algorithm import BacktrackingColouringAlgorithm
from graph_colouring_algorithms.forward_checking_algorithm import ForwardCheckingAlgorithm
from my_error import MyError
import matplotlib.pyplot as plt


def main():
    try:
        plt.rc('axes', axisbelow=True)

        number_of_iterations = 50
        graph_parameters = [[100, 0.2], [100, 0.5], [100, 0.8]]

        for max_number_of_vertices, probability in graph_parameters:
            greedy_times_for_vertices = []
            wp_times_for_vertices = []
            dsatur_times_for_vertices = []

            greedy_colors_for_vertices = []
            wp_colors_for_vertices = []
            dsatur_colors_for_vertices = []

            number_of_vertices_list = [i for i in range(1, max_number_of_vertices + 1)]

            for number_of_vertices in number_of_vertices_list:
                greedy_time = 0
                wp_time = 0
                dsatur_time = 0

                greedy_colors = 0
                wp_colors = 0
                dsatur_colors = 0
                for _ in range(number_of_iterations):
                    graph: Graph = RandomGraphGenerator.generate_for_vertices(number_of_vertices, probability)

                    graph.set_graph_colouring_algorithm(GreedyColouringAlgorithm())
                    greedy_time += graph.colour()
                    greedy_colors += graph.get_number_of_colours()

                    graph.set_graph_colouring_algorithm(WelshPowellColouringAlgorithm())
                    wp_time += graph.colour()
                    wp_colors += graph.get_number_of_colours()

                    graph.set_graph_colouring_algorithm(DSaturColouringAlgorithm())
                    dsatur_time += graph.colour()
                    dsatur_colors += graph.get_number_of_colours()

                greedy_times_for_vertices.append(greedy_time / number_of_iterations * 1000)
                wp_times_for_vertices.append(wp_time / number_of_iterations * 1000)
                dsatur_times_for_vertices.append(dsatur_time / number_of_iterations * 1000)

                greedy_colors_for_vertices.append(greedy_colors / number_of_iterations)
                wp_colors_for_vertices.append(wp_colors / number_of_iterations)
                dsatur_colors_for_vertices.append(dsatur_colors / number_of_iterations)

            plt.figure(1)
            plt.grid()
            plt.plot(number_of_vertices_list, greedy_times_for_vertices, label='Greedy', color='blue')
            plt.plot(number_of_vertices_list, wp_times_for_vertices, label='Welsh-Powell', color='red',
                     linestyle='--')
            plt.plot(number_of_vertices_list, dsatur_times_for_vertices, label='DSatur', color='green')
            plt.title(f'Вероватноћа гране = {probability}')
            plt.xlabel('Број чворова')
            plt.ylabel('Време [ms]')
            plt.legend()
            plt.show()

            plt.figure(2)
            plt.grid()
            plt.plot(number_of_vertices_list, greedy_colors_for_vertices, label='Greedy', color='blue')
            plt.plot(number_of_vertices_list, wp_colors_for_vertices, label='Welsh-Powell', color='red')
            plt.plot(number_of_vertices_list, dsatur_colors_for_vertices, label='DSatur', color='green',
                     linestyle='--')
            plt.title(f'Вероватноћа гране = {probability}')
            plt.xlabel('Број чворова')
            plt.ylabel('Број боја')
            plt.legend()
            plt.show()

        number_of_iterations = 50
        graph_parameters = [[25, 0.2], [20, 0.5], [10, 0.8]]

        for max_number_of_vertices, probability in graph_parameters:
            greedy_times_for_vertices = []
            backtracking_times_for_vertices = []

            greedy_colors_for_vertices = []
            backtracking_colors_for_vertices = []

            number_of_vertices_list = [i for i in range(1, max_number_of_vertices + 1)]

            for number_of_vertices in number_of_vertices_list:
                greedy_time = 0
                backtracking_time = 0

                greedy_colors = 0
                backtracking_colors = 0
                for _ in range(number_of_iterations):
                    graph: Graph = RandomGraphGenerator.generate_for_vertices(number_of_vertices, probability)

                    graph.set_graph_colouring_algorithm(GreedyColouringAlgorithm())
                    greedy_time += graph.colour()
                    greedy_colors += graph.get_number_of_colours()

                    graph.set_graph_colouring_algorithm(BacktrackingColouringAlgorithm())
                    backtracking_time += graph.colour()
                    backtracking_colors += graph.get_number_of_colours()

                greedy_times_for_vertices.append(greedy_time / number_of_iterations * 1000)
                backtracking_times_for_vertices.append(backtracking_time / number_of_iterations * 1000)

                greedy_colors_for_vertices.append(greedy_colors / number_of_iterations)
                backtracking_colors_for_vertices.append(backtracking_colors / number_of_iterations)

            plt.figure(1)
            plt.grid()
            plt.plot(number_of_vertices_list, greedy_times_for_vertices, label='Greedy', color='blue')
            plt.plot(number_of_vertices_list, backtracking_times_for_vertices, label='Backtracking', color='red',
                     linestyle='--')
            plt.title(f'Вероватноћа гране = {probability}')
            plt.xlabel('Број чворова')
            plt.ylabel('Време [ms]')
            plt.legend()
            plt.show()

            plt.figure(2)
            plt.grid()
            plt.plot(number_of_vertices_list, greedy_colors_for_vertices, label='Greedy', color='blue')
            plt.plot(number_of_vertices_list, backtracking_colors_for_vertices, label='Backtracking', color='red',
                     linestyle='--')
            plt.title(f'Вероватноћа гране = {probability}')
            plt.xlabel('Број чворова')
            plt.ylabel('Број боја')
            plt.legend()
            plt.show()

        graph_parameters = [[25, 0.2, 50], [20, 0.5, 20], [15, 0.8, 10]]

        for max_number_of_vertices, probability, iterations in graph_parameters:
            fc_times_for_vertices = []
            bt_times_for_vertices = []
            speedups_for_vertices = []

            number_of_vertices_list = [i for i in range(1, max_number_of_vertices + 1)]

            for number_of_vertices in number_of_vertices_list:
                fc_time = 0
                bt_time = 0
                for _ in range(iterations):
                    graph: Graph = RandomGraphGenerator.generate_for_vertices(number_of_vertices, probability)

                    graph.set_graph_colouring_algorithm(ForwardCheckingAlgorithm())
                    fc_time += graph.colour()

                    graph.set_graph_colouring_algorithm(BacktrackingColouringAlgorithm())
                    bt_time += graph.colour()

                fc_times_for_vertices.append(fc_time / iterations)
                bt_times_for_vertices.append(bt_time / iterations)
                speedups_for_vertices.append(bt_time / fc_time)

            plt.figure(1)
            plt.grid()
            plt.plot(number_of_vertices_list, fc_times_for_vertices, label='Forward Checking', color='blue')
            plt.plot(number_of_vertices_list, bt_times_for_vertices, label='Backtracking', color='red',
                     linestyle='--')
            plt.title(f'Вероватноћа гране = {probability}')
            plt.xlabel('Број чворова')
            plt.ylabel('Време [s]')
            plt.legend()
            plt.show()

            plt.figure(2)
            plt.grid()
            plt.plot(number_of_vertices_list, speedups_for_vertices, color='red')
            plt.title(f'Вероватноћа гране = {probability}')
            plt.xlabel('Број чворова')
            plt.ylabel('Убрзање')
            plt.show()

    except MyError as e:
        print(e)


if __name__ == "__main__":
    main()
