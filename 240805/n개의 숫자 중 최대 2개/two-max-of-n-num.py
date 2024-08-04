n = int(input())

arr = list(map(int, input().split()))
import sys
max = -sys.maxsize
max2 = -sys.maxsize
arr2 =[]

for i in arr:
    if i >max:
        max = i
        
for i in arr:
    if i != max:
        if i >max2:
            max2 = i

print(max, max2)