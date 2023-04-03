# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]
#
#
# def union(x, y):
#     x = find(x)
#     y = find(y)
#     if x < y:
#         parent[y] = x
#     else:
#         parent[x] = y
#
#
# v, e, turn = map(int, input().strip().split())
#
# edge_list = []
# for i in range(1, e + 1):
#     a, b = map(int, input().strip().split())
#     edge_list.append((i, a, b))
#
# edge_list.sort()
#
# result_list = []
# for t in range(turn):
#     parent = [0] * (v + 1)
#
#     for i in range(1, v + 1):
#         parent[i] = i
#
#     for i in range(check):
#         parent[check[i][0]]
#     cost_list = []
#     cost_check = [True] * (v + 1)
#
#     result = 0
#     for edge in edge_list:
#         cost, a, b = edge
#         if find(a) != find(b):
#             union(a, b)
#             result += cost
#             cost_list.append(cost)
#     result_list.append(result)
#     if len(cost_list) != 0:
#
# for r in result_list:
#     print(r, end=" ")
