n = int(input())

arr = list(map(int, input().split()))

import sys
max_val = -1


for i in arr:
    if i > max_val:
        cnt =0
        for j in arr:
            if j == i:
                cnt +=1
        if cnt ==1:
            max_val = i 

print(max_val)