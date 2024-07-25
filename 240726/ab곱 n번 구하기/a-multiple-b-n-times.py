n = int(input())
sum_val=1

for i in range(n):
    a, b = map(int, input().split())

    for j in range(a, b+1):
        sum_val *= j
    print(sum_val)

    sum_val=1