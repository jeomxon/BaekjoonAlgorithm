import sys
input = sys.stdin.readline


def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


num_card = int(input())
card_list = list(map(int, input().strip().split()))
num = int(input())
num_list = list(map(int, input().strip().split()))

card_dict = {}
for i in card_list:
    if i not in card_dict:
        card_dict[i] = 1
    else:
        card_dict[i] += 1

sorted_card = sorted(card_dict.items())
print(sorted_card)

result_list = []
for i in range(len(num_list)):
    if binary_search(num_list[i], sorted_card) is not None:
        result_list.append(1)
    else:
        result_list.append(0)

print(result_list)
