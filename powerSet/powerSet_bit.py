arr = [1, 2, 3, 4, 5, 6]
n = len(arr)

for i in range(1<<n):
    tmp = []
    for j in range(n):
        if i & (1<<j):
            tmp.append(arr[j])
    print(tmp)