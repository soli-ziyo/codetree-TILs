arr1=[]; arr2=[]
arr_2d = [[0 for _ in range(3)] for  _ in range(3)]

for i in range(3):
    arr = list(map(int, input().split()))
    arr1.append(arr)
input() #비어있는 한줄을 입력받아야함 
for i in range(3):
    arr = list(map(int, input().split()))
    arr2.append(arr)

for i in range(3):
    for j in range(3):
        k = arr1[i][j] * arr2[i][j]
        arr_2d[i][j] = k

for i in range(3):
    for j in range(3):
        print(arr_2d[i][j], end=' ')
    print()