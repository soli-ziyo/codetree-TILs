arr1 = input().split()
a1 = int(arr1[0])
a2 = int(arr1[1])

arr2 = input().split()
b1 = int(arr2[0])
b2 = int(arr2[1])

if a1 >b1:
    print("A")
elif a1 == b1 and a2 > b2:
    print("A")
elif b1>a1:
    print("B")
elif a1 == b1 and b2>a2:
    print("B")