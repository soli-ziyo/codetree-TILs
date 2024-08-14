arr = list(map(int, input().split()))

for i in range(2, min(arr)+1):
    if (max(arr) * i) % min(arr) == 0:
        print(max(arr)*i)
        break
    else:
        continue