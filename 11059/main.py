s = input()

part = []
for i in range(len(s)):
    for j in range(i, len(s)):
        sub_list = s[i:j+1]
        part.append(sub_list)

even_part = []
for s in part:
    if len(s) % 2 == 0:
        even_part.append(s)

answer = []
for s in even_part:
    a = s[:len(s) // 2]
    b = s[len(s) // 2:]

    a_sum = 0
    b_sum = 0
    for i in range(len(a)):
        a_sum += int(a[i])
        b_sum += int(b[i])

    if a_sum == b_sum:
        answer.append(s)

print(len(max(answer, key=len)))

