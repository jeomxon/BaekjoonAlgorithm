import sys
sys.setrecursionlimit(10**5)


def dfs(x, y):
    if x < 0 or x >= row or y < 0 or y >= col:
        return False

    if matrix[x][y] == 1:
        matrix[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True

    return False


num_test = int(input())

index = 0
while index != num_test:
    col, row, check = map(int, input().strip().split())

    check_list = []
    for i in range(check):
        check_list.append(list(map(int, input().strip().split())))

    matrix = []
    for r in range(row):
        temp_list = []
        for c in range(col):
            temp_list.append(0)
        matrix.append(temp_list)

    for i in range(len(check_list)):
        matrix[check_list[i][1]][check_list[i][0]] = 1

    result = 0
    for r in range(row):
        for c in range(col):
            if dfs(r, c):
                result += 1

    print(result)

    index += 1
