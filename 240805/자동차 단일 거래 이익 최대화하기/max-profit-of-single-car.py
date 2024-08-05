n = int(input())

arr = list(map(int, input().split()))

import sys
min_val = sys. maxsize
index = 0
for i in range(n):
    if arr[i] < min_val:
        min_val = arr[i] 
        idx= i
max_val = min_val

if idx == n-1:
    print(0)
else:
    for j in range(idx, n):
        if arr[j] > max_val:
            max_val = arr[j]
    print(max_val-min_val)