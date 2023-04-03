import sys
INF = int(1e9)

N, M = map(int, input().strip().split())

graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().strip().split())
    graph[a][b] = 1
    graph[b][a] = 1

print(graph)

for k in range(N+1):
    graph[k][k] = 0
    for i in range(N+1):
        for j in range(N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

print(graph)

result = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i != j:
            result[i] += graph[i][j]

print(result.index(min(result[1:])))
