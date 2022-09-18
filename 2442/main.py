n = int(input())

count = 1
for i in range(n-1, -1, -1):
    for j in range(i):
        print(end=" ")
    print("*" * (2 * count - 1))
    count += 1
