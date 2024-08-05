n = int(input())
arr = list(map(int, input().split()))

result = -1

while result != 0:
    result = arr.index(max(arr[0:result]))
    print(result +1, end = " ")