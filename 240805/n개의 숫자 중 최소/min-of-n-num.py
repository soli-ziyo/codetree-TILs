n = int(input())

arr = list(map(int, input().split()))
import sys 
min = sys.maxsize
cnt =0

for i in arr:
    if i <min:
        min =i

for i in arr:
    if i == min:
        cnt +=1

print(min, end=' ')
print(cnt)