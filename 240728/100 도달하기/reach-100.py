n = int(input())
arr =[1, n]

for i in range(100):
    sum = arr[-1]+arr[-2]
    if sum >=100:
        arr.append(sum)
        break
    else:
        arr.append(sum)

for j in arr:
    print(j , end=' ')