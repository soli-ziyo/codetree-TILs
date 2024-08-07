n, m = map(int, input().split())

arr = [[0 for i in range(n+1)] for j in range(n+1)]
cnt =1
for i in range(m):
    r, c = tuple(map(int, input().split()))
    
    for j in range(n+1):
        arr[r][c] =cnt 
    cnt +=1

for i in range(1, n+1):
    for j in range(1, n+1):
        print(arr[i][j], end=' ')
    print()