"""
Write a python program called "q1.py" that accepts as an argument
an input file containing the locations of the cities and highways,
a starting city and a destination city.
Your program should output the length of the shortest path between the starting city and
the destination. If no path exists, it should output "NO PATH EXISTS".
You should use the A* algorithm with any non-trivial admissible heuristic of your choice.
"""

import yaml
import math


def yaml_loader():
    with open("sample-input.yaml", 'r') as yaml_input_file:
        try:
            data = yaml.load(yaml_input_file, Loader=yaml.FullLoader)
        except yaml.YAMLError as exc:
            print("Error in configuration file:", exc)

    return data


def euclidean_distance(a, b):
    """
    Euclidean Heuristic used.
    :param a:
    :param b:
    :return:
    """

    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def main():
    data = yaml_loader()

    dict_cities = data.get('cities')
    highways = data.get('highways')

    start_state = data.get('start')
    goal_state = data.get('end')
    frontier = [start_state]
    # f = g + h = 0 for the initial state.
    f_cost = [0]
    g_cost = [0]
    explored_set = []

    path_exists = False
    for loc1, loc2 in highways:
        if loc1 == goal_state or loc2 == goal_state:
            path_exists = True

    if not path_exists:
        print("NO PATH EXISTS.")
    else:
        while frontier:
            if frontier[0] == goal_state:  # Goal state found
                explored_set.append(goal_state)
                break

            for loc1, loc2 in highways:
                if loc1 == frontier[0] or loc2 == frontier[0]:

                    if loc1 == frontier[0]:
                        g_tmp = g_cost[0] + euclidean_distance(dict_cities[loc1], dict_cities[loc2])
                        h_tmp = euclidean_distance(dict_cities[loc2], dict_cities[goal_state])
                        frontier.append(loc2)
                    else:
                        g_tmp = g_cost[0] + euclidean_distance(dict_cities[loc2], dict_cities[loc1])
                        h_tmp = euclidean_distance(dict_cities[loc1], dict_cities[goal_state])
                        frontier.append(loc1)

                    g_cost.append(g_tmp)
                    f_cost.append(g_tmp + h_tmp)

            explored_set.append(frontier[0])
            frontier.pop(0)
            g_cost.pop(0)
            f_cost.pop(0)

            for index, item in enumerate(f_cost):
                if item == min(f_cost):
                    tmp = frontier[0]
                    frontier[0] = frontier[index]
                    frontier[index] = tmp

                    tmp = g_cost[0]
                    g_cost[0] = g_cost[index]
                    g_cost[index] = tmp

                    tmp = f_cost[0]
                    f_cost[0] = f_cost[index]
                    f_cost[index] = tmp

    if path_exists:
        print(f_cost[0])


if __name__ == "__main__":
    main()
