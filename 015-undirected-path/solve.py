# depth first solution
def undirected_path(edges, node_A, node_B):
    graph = build_graph(edges)
    return has_path(graph, node_A, node_B, set())

def build_graph(edges):
    graph = {}
    
    for edge in edges:
        a, b = edge
        
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)
    
    return graph
    
def has_path(graph, src, dst, visited):
    if src == dst:
        return True
        
    if src in visited:
        return False
    
    visited.add(src)
    
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst, visited) == True:
            return True
    
    return False


# Testing
edges = [
    ('i', 'j'),
    ('k', 'i'),
    ('m', 'k'),
    ('k', 'l'),
    ('o', 'n')
]

print(undirected_path(edges, 'j', 'm')) # True
print(undirected_path(edges, 'm', 'j')) # True
print(undirected_path(edges, 'l', 'j')) # True
print(undirected_path(edges, 'k', 'o')) # False
print(undirected_path(edges, 'i', 'o')) # False

# n = number of nodes
# e = number of edges
# Time: O(e)
# Space: O(n)