arr= list(map(int, input().split()))

import sys
max = -sys.maxsize ; min = sys.maxsize

for i in arr:
    if i > 500:
        if i < min:
            min = i
    elif i < 500:
        if i >max:
            max = i

print(max, min)