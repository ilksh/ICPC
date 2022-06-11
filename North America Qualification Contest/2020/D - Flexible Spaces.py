used = [False for _ in range(101)]
partition = []

w, p = map(int, input().split())    # width, number of partition
temp = list(map(int, input().split()))

partition.append(0)
for elem in temp:
    partition.append(elem)
partition.append(w)

for i in range(p+2):
    for j in range(i+1, p+2):
        length = partition[j] - partition[i]
        used[length] = True

for data in range(w+1):
    if used[data]:
        print(data, end=" ")




