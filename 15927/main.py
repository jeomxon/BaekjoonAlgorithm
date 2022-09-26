word = input()
real_answer = 0

answer = True
for i in range(len(word) // 2):
    if word[i] != word[-(i+1)]:
        answer = False

if answer == True:
    temp = word[0]
    for i in word:
        if temp != i:
            real_answer = 1
        temp = i

    if real_answer != 1:
        print(-1)
    else:
        print(len(word)-1)
else:
    print(len(word))
