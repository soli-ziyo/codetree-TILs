arr = list(map(int, input().split()))

for i in range(8):
    sum = arr[-1]+(2*arr[-2])
    arr.append(sum)

for j in arr:
    print(j, end=' ')