n = int(input())

arr= list(map(int, input().split()))
import sys
min_val = sys.maxsize

for i in range(n):
    for j in range(i+1, n):
        if abs(arr[i]- arr[j]) < min_val:
            min_val = abs(arr[i]- arr[j])

print(min_val)