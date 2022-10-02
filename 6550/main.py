while True:
    try:
        a, b = input().strip().split()

        index = 0
        for alph in b:
            if a[index] == alph:
                index += 1
            if index == len(a):
                print("Yes")
                break

        if index != len(a):
            print("No")

    except EOFError:
        break
