n, m = map(int, input().split())
arr = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    r, c = tuple(map(int, input().split()))

    for j in range(n+1):
        arr[r][c] =1

for i in range(1, n+1):
    for j in range(1, n+1):
        print(arr[i][j], end= ' ')
    print()