from collections import deque


# breadth first solution
def has_path(graph, src, dst):
    queue = deque([ src ])
    
    while queue:
        current = queue.popleft()

        if current == dst:
            return True
        
        for neighbor in graph[current]:
            queue.append(neighbor)
    
    return False


graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

print(has_path(graph, 'f', 'k')) # True
print(has_path(graph, 'f', 'j')) # False

# n = number of nodes
# e = number of edges
# Time: O(e)
# Space: O(n)