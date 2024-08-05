for i in range(5):
    arr2 =[]
    arr = list(input().split())

    for j in arr:
        arr2.append(j.upper())

    for i in arr2:
        print(i, end=' ')
    print('')