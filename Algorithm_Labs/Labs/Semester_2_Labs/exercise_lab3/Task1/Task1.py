def topological_sort(graph):
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        order.append(node)

    visited = set()
    order = []
    for node in graph:
        if node not in visited:
            dfs(node)
    return order[::-1]

# Чтение входных данных из файла
with open('input.txt', 'r') as file:
    n, m = map(int, file.readline().split())
    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, file.readline().split())
        graph[u].append(v)

# Получение топологического порядка
topological_order = topological_sort(graph)

# Запись результата в файл
with open('output.txt', 'w') as file:
    file.write(" ".join(map(str, topological_order)))
