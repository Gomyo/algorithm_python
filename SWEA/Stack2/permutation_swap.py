arr = [1,2,3]
N = 3

def perm(idx):
    if idx == N:
        print(arr)
    else:
        for i in range(idx, N):
            arr[idx], arr[i] = arr[i], arr[idx] # 순서변경
            perm(idx + 1)
            arr[idx], arr[i] = arr[i], arr[idx] # 원상복귀

perm(0)