def read_input(filename):
    with open(filename, 'r') as file:
        n, m = map(int, file.readline().split())
        edges = [tuple(map(int, file.readline().split())) for _ in range(m)]
    return n, m, edges


def kosaraju_scc(n, edges):
    from collections import defaultdict, deque

    def dfs(v, graph, visited, stack=None):
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                dfs(u, graph, visited, stack)
        if stack is not None:
            stack.append(v)

    graph = defaultdict(list)
    reverse_graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        reverse_graph[v].append(u)

    visited = [False] * (n + 1)
    stack = []

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, graph, visited, stack)

    visited = [False] * (n + 1)
    scc = []

    while stack:
        v = stack.pop()
        if not visited[v]:
            component = []
            dfs(v, reverse_graph, visited, component)
            scc.append(component)

    return scc


def min_k_for_weakly_k_connected(n, edges):
    scc = kosaraju_scc(n, edges)
    component_count = len(scc)

    if component_count == 1:
        return '0'

    component_map = {}
    for i, component in enumerate(scc):
        for node in component:
            component_map[node] = i

    from collections import defaultdict
    in_degree = [0] * component_count
    out_degree = [0] * component_count

    for u, v in edges:
        if component_map[u] != component_map[v]:
            out_degree[component_map[u]] += 1
            in_degree[component_map[v]] += 1

    source_count = sum(1 for i in range(component_count) if in_degree[i] == 0)
    sink_count = sum(1 for i in range(component_count) if out_degree[i] == 0)

    return '1' if max(source_count, sink_count) > 0 else '0'


def main():
    n, m, edges = read_input('input.txt')
    result = min_k_for_weakly_k_connected(n, edges)
    with open('output.txt', 'w') as file:
        file.write(f'{result}\n')


if __name__ == "__main__":
    main()
