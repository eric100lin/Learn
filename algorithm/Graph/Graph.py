def dfs(graph, vertex, visited = set()):
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, vertex):
    import collections
    q = collections.deque()
    q.append(vertex)
    visited = { vertex }
    while q:
        v = q.popleft()
        print(v, end=' ')
        for neighbor in graph[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(graph, 'A')
print()

bfs(graph, 'A')
print()