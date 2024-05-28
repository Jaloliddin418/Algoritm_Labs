def has_negative_cycle(graph, n):
    distance = [float('inf')] * n
    distance[0] = 0  # Начальная вершина
    for _ in range(n - 1):
        for u, v, weight in graph:
            if distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
    for u, v, weight in graph:
        if distance[u] + weight < distance[v]:
            return 1
    return 0


def main():
    with open('input.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        graph = []
        for _ in range(m):
            u, v, weight = map(int, f.readline().split())
            graph.append((u - 1, v - 1, weight))

    result = has_negative_cycle(graph, n)

    with open('output.txt', 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    main()
