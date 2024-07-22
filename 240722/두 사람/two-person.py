arr = input().split()
age1 = int(arr[0])
gender1 = arr[1]

arr2 = input().split()
age2 = int(arr2[0])
gender2 = arr2[1]

if (age1 >=19 or age2 >= 19) and (gender1 == "M" or gender2 == "M"):
    print(1)
else:
    print(0)