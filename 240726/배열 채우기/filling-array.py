arr =[]
reversed_arr =[]

mylist =list(map(int, input().split()))

for i in mylist:
    if i !=0:
        arr.append(i)
    else:
        break

reversed_arr = arr[::-1]
k = len(reversed_arr)

for i in reversed_arr:
    print(i, end=' ')