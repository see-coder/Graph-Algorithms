def depth_first_print(graph, start):
    stack = [ start ]
    while len(stack) > 0:
        current = stack[-1]
        print(current)
        stack.pop()
        for neighbor in graph[current]:
            stack.append(neighbor)


graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

depth_first_print(graph, 'a')