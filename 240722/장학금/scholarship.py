arr = input().split()
a = int(arr[0])
b = int(arr[1])

if a>=90:
    c=1
else:
    c=0

if c==1 and b>=95:
    print(100000)
elif c==1 and b>=90:
    print(50000)
else:
    print(0)