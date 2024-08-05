n = int(input())
arr = [[1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(1, i+1):
        if j ==i:
            arr[i][j] =1
        else:
            arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

for i in range(n):
    for j in range(i+1):
        print(arr[i][j], end=' ')
    print()