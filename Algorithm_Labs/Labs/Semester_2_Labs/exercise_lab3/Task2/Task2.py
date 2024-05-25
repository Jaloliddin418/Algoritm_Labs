import math


def read_input(filename):
    with open(filename, 'r') as f:
        n, m = map(int, f.readline().split())
        edges = []
        for _ in range(m):
            u, v, r = map(float, f.readline().split())
            edges.append((int(u), int(v), r))
    return n, edges


def bellman_ford(n, edges, start, debug_file):
    dist = [float('inf')] * n
    dist[start] = 0
    debug_file.write(f"Starting Bellman-Ford from vertex {start}\n")
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                debug_file.write(f"Updated distance: dist[{v}] = {dist[v]}\n")

    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            debug_file.write(f"Negative cycle detected: edge ({u}, {v}) with weight {w}\n")
            return True  # Negative cycle detected
    return False


def main():
    n, edges = read_input('input.txt')

    # Open debug file
    with open('debug.txt', 'w') as debug_file:
        # Convert weights from rij to -log(rij)
        log_edges = []
        for u, v, r in edges:
            if r <= 0:
                debug_file.write(f"Skipping invalid exchange rate: r[{u},{v}] = {r}\n")
                continue
            log_edges.append((u - 1, v - 1, -math.log(r)))

        debug_file.write("Log edges:\n")
        for edge in log_edges:
            debug_file.write(f"{edge}\n")

        # Check for negative cycles from any starting vertex
        for i in range(n):
            if bellman_ford(n, log_edges, i, debug_file):
                with open('output.txt', 'w') as f:
                    f.write('1\n')
                debug_file.write("Negative cycle found\n")
                return

        with open('output.txt', 'w') as f:
            f.write('0\n')
        debug_file.write("No negative cycle found\n")


if __name__ == "__main__":
    main()
