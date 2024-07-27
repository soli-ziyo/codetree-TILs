n, m= map(int, input().split())

arr = list(map(int, input().split()))
count =0

for i in arr:
    if m in arr:
        count = arr.count(m)
    else:
        continue

print(count)