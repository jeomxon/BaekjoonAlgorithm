n = int(input())

count = 0
for i in range(n, 0, -1):
    for j in range(count):
        print(end=" ")

    print("*" * (2*i-1), end="")
    print()
    count += 1
