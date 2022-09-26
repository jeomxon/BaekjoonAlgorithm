def inf(a, b):

    min_mult = 0
    for i in range(max(len(a), len(b)), len(a)*len(b)+1):
        if i % len(a) == 0 and i % len(b) == 0:
            min_mult = i
            break

    new_a = min_mult // len(a)
    new_b = min_mult // len(b)

    if a * new_a == b * new_b:
        return 1
    return 0


if __name__ == '__main__':
    a, b = input(), input()
    print(inf(a, b))


# second short coding
# a,b=input(),input()
# print(int(a*len(b)==b*len(a)))

# short coding
# print(+((input()*99)[:99]==(input()*99)[:99]))

