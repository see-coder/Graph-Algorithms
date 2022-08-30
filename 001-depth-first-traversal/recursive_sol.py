def depth_first_print(graph, current):
    print(current)
    for neighbor in graph[current]:
        depth_first_print(graph, neighbor)


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

depth_first_print(graph, 'a')