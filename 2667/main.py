n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]
apartment_block = []

x_point = [-1, 1, 0, 0]
y_point = [0, 0, -1, 1]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if matrix[x][y] == 1:
        global count
        count += 1
        matrix[x][y] = 0
        for i in range(4):
            new_x = x + x_point[i]
            new_y = y + y_point[i]
            dfs(new_x, new_y)
        return True
    return False


count = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            apartment_block.append(count)
            count = 0

print(len(apartment_block))
for i in sorted(apartment_block):
    print(i)
