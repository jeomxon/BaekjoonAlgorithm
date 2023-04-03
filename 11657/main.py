import sys

input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().strip().split())

graph = []
for i in range(E):
    a, b, c = map(int, input().strip().split())
    graph.append((a, b, c))

distances = [INF] * (V+1)


def bellman_ford(graph, start):
    distances[start] = 0

    for i in range(V):
        for j in range(E):
            current_node, next_node, cost = graph[j]

            if distances[current_node] != INF and distances[next_node] > distances[current_node] + cost:
                distances[next_node] = distances[current_node] + cost

                if i == V - 1:
                    return True

    return False


if bellman_ford(graph, 1):
    print(-1)
else:
    for i in range(2, V + 1):
        if distances[i] == INF:
            print(-1)
        else:
            print(distances[i])
