arr= input().split()
a, b = int(arr[0]), int(arr[1])

c = (10000*b) / (a*a)
print(int(c))
if c>=25:
    print("Obesity")