arr_2d = []

for i in range(4):
    arr_1d = list(map(int, input().split()))

    arr_2d.append(arr_1d)

cnt =1
sum =0

for i in range(4):
    for j in range(cnt):
        sum += arr_2d[i][j]
    cnt +=1

print(sum)