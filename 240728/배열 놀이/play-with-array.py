n, q = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(q):
    mylist = list(map(int, input().split()))
    if mylist[0] ==1:
        print(arr[mylist[1]-1])
    elif mylist[0] ==2:
        if mylist[1] in arr:
            print(arr.index(mylist[1])+1)
        else:
            print(0)
    elif mylist[0] ==3:
        for j in range(mylist[1], mylist[2]+1):
            print(arr[j-1], end=' ')
        print()