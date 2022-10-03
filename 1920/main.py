from sys import stdin
total = stdin.readline()
num_list = set(stdin.readline().split())
check_num = stdin.readline()
check_list = stdin.readline().split()

for i in check_list:
    if i in num_list:
        print(1)
    else:
        print(0)