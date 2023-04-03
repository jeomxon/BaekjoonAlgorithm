N, M = map(int, input().strip().split())

truth_set = set(input().strip().split()[1:])

parties = []
for _ in range(M):
    parties.append(set(input().strip().split()[1:]))

for _ in range(M):
    for party in parties:
        if party.intersection(truth_set):
            truth_set = truth_set.union(party)

count = 0
for party in parties:
    if not party.intersection(truth_set):
        count += 1

print(count)
