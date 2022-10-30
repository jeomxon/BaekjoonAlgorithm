def dfs(graph, start_node):
    visit = []
    stack = []

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit

def bfs(graph, start_node):
    visit = []
    queue = []

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit


num_node, num_edge, start_node = map(int, input().strip().split())
graph = {}

for i in range(1, num_node+1):
    graph[i] = []

for i in range(num_edge):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)


for node in graph:
    graph[node].sort(reverse=True)

des_graph = graph.copy()

print(*dfs(des_graph, start_node))

for node in graph:
    graph[node].sort()

asd_graph = graph.copy()

print(*bfs(asd_graph, start_node))
