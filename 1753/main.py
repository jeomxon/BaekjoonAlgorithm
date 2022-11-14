import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


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


V, E = map(int, input().strip().split())
start = int(input())

graph = {}
for i in range(E):
    a, b, c = map(int, input().strip().split())
    if a not in graph:
        graph[a] = {b: c}
    else:
        if b in graph[a]:
            if graph[a][b] < c:
                continue
        graph[a][b] = c

for i in range(1, V + 1):
    if i not in graph:
        graph[i] = {}

result_graph = dijkstra(graph, start)

result_list = [0] * V
for node in result_graph:
    result_list[node-1] = result_graph[node]


for i in result_list:
    if i == INF:
        print("INF")
    else:
        print(i)
