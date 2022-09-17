def hanoi(n, from_pole, temp_pole, to_pole):

    if n == 1:
        print(from_pole, to_pole)
        return

    hanoi(n-1, from_pole, to_pole, temp_pole)

    print(from_pole, to_pole)

    hanoi(n-1, temp_pole, from_pole, to_pole)


num = int(input())
print(2**num-1)
hanoi(num, 1, 2, 3)

