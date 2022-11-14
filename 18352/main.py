import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline


def dijkstra(graph, start):
    distances = {node: INF for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance

            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances


V, E, K, start = map(int, input().strip().split())

graph = {}
for i in range(E):
    a, b = map(int, input().strip().split())
    if a not in graph:
        graph[a] = {b: 1}
    else:
        graph[a][b] = 1

for node in range(1, V + 1):
    if node not in graph:
        graph[node] = {}

result_graph = dijkstra(graph, start)
result_list = []
for node in result_graph:
    if result_graph[node] == K:
        result_list.append(node)

if len(result_list) == 0:
    print(-1)
else:
    result_list.sort()
    for r in result_list:
        print(r)
