from collections import deque


def breadth_first_print(graph, start):
    queue = deque([ start ])
    while len(queue) > 0:
        current = queue[0]
        print(current)
        queue.popleft()
        for neighbor in graph[current]:
            queue.append(neighbor)


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

breadth_first_print(graph, 'a')

# Breadth first requires some sort of like a queue data structure.
# But if you try to write recursion it always inherently has the underlying stack(recursive call stack).
# So you're always gonna have to fight against that if you're trying to implement breadth first using recursion.
# So it's not really worth doing.