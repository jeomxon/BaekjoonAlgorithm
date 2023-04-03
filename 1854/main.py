import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(graph, start):
    dp = [[INF] * K for _ in range(V + 1)]
    dp[start][0] = 0
    heap = []
    heapq.heappush(heap, [dp[start][0], start])

    while heap:
        current_distance, current_destination = heapq.heappop(heap)

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance

            if distance < dp[new_destination][K-1]:
                dp[new_destination][K-1] = distance
                dp[new_destination].sort()
                heapq.heappush(heap, [distance, new_destination])

    return dp


V, E, K = map(int, input().strip().split())

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

result_list = dijkstra(graph, 1)

for i in range(1, V + 1):
    if result_list[i][K-1] == INF:
        print(-1)
    else:
        print(result_list[i][K-1])
