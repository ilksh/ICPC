used = [False for _ in range(101)]

w, p = map(int, input().split())    # width, number of partition
partition = [0 for _ in range(p+1)]
temp = list(map(int, input().split()))

partition[0] = 0
idx = 1
for elem in partition:
    partition[idx] = elem
    idx += 1
partition.append(w)

for i in range(p+2):
    for j in range(i+1, p+2):
        length = partition[j] - partition[i]
        used[length] = True

for data in range(w+1):
    if used[data]:
        print(data, end=" ")




