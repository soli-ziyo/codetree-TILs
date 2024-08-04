n = int(input())

arr = list(map(int, input().split()))
import sys
max = -sys.maxsize
max2 = -sys.maxsize
arr2 =[]
cnt = 0
for i in arr:
    if i >max:
        max = i

for i in arr:
    if i ==max:
        cnt +=1 

for i in arr:
    if cnt ==1:
        if i != max and i >max2:
            max2 = i
    else:
        max2 = max

print(max, max2)